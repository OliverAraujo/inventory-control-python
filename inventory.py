"""Inventory rules, independent from terminal input and file storage."""

def normalize_name(name):
    if not isinstance(name, str) or not name.strip():
        raise ValueError("The product name cannot be empty.")
    return name.strip().lower()


def validate_quantity(quantity, allow_zero=False):
    minimum = 0 if allow_zero else 1
    if type(quantity) is not int or quantity < minimum:
        raise ValueError("Enter a whole number greater than or equal to " + str(minimum) + ".")


def register_product(products, name, quantity):
    name = normalize_name(name)
    validate_quantity(quantity, allow_zero=True)
    if name in products:
        raise ValueError("This product is already registered.")
    products[name] = quantity


def record_entry(products, name, quantity):
    name = normalize_name(name)
    validate_quantity(quantity)
    if name not in products:
        raise ValueError("Product not found. Register it first.")
    products[name] += quantity


def record_issue(products, name, quantity):
    name = normalize_name(name)
    validate_quantity(quantity)
    if name not in products:
        raise ValueError("Product not found.")
    if quantity > products[name]:
        raise ValueError("Insufficient stock.")
    products[name] -= quantity
