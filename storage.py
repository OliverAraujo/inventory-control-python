"""JSON persistence for a single running inventory application."""
import json
import os
import tempfile
from pathlib import Path
from inventory import normalize_name, validate_quantity

DEFAULT_PATH = Path(__file__).resolve().parent / "data" / "inventory.json"


def validate_products(products):
    if not isinstance(products, dict):
        raise ValueError("Inventory must be a JSON object.")
    for name, quantity in products.items():
        if normalize_name(name) != name:
            raise ValueError("Stored product names must be normalized.")
        validate_quantity(quantity, allow_zero=True)


def load_inventory(path=DEFAULT_PATH):
    path = Path(path)
    try:
        with path.open(encoding="utf-8") as source:
            products = json.load(source)
    except FileNotFoundError:
        return {}
    validate_products(products)
    return products


def save_inventory(products, path=DEFAULT_PATH):
    validate_products(products)
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8",
                                         dir=path.parent, delete=False) as target:
            temporary = Path(target.name)
            json.dump(products, target, ensure_ascii=False, indent=2)
            target.write("\n")
            target.flush()
            os.fsync(target.fileno())
        os.replace(temporary, path)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)
