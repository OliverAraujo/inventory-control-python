# Inventory Control with Python

A terminal application for product registration, incoming and outgoing stock, and stock lookup. Learning project using Python 3.10+ and the standard library.

## Run

```bash
git clone https://github.com/OliverAraujo/inventory-control-python.git
cd inventory-control-python
python main.py
```

On Windows you can use `py main.py`. Enter Y to open the menu (this is confirmation, not authentication).

1. Register a product with an initial quantity.
2. Record incoming stock.
3. Record outgoing stock.
4. View inventory.
5. Exit.

## Example to reproduce

Register mouse with 10 units, receive 5, and remove 3. Option 4 shows `mouse: 12 unit(s)`. Close and restart the application: the 12 units are still there.

## Design decisions

- A dictionary maps each product name to its stock quantity for direct lookup.
- Names are trimmed and converted to lowercase, so Mouse and mouse refer to the same product.
- Business rules live in `inventory.py`, separately from terminal input.
- JSON is a small, readable first step toward persistence without a database.
- Each successful operation is saved automatically to `data/inventory.json`.
- A temporary file followed by replacement protects the previous file from partial writes.
- The interface updates its in-memory stock only after saving succeeds.
- Invalid or unreadable stored data stops startup with an error; it is not silently erased.

## Rules

Names cannot be blank or duplicated. Initial quantities must be nonnegative integers. Movements must be positive integers. Withdrawals cannot exceed stock. Invalid operations do not change inventory.

## Structure

- `main.py`: terminal menu and user messages.
- `inventory.py`: registration and movement rules.
- `storage.py`: JSON validation, loading and saving.
- `tests/test_inventory.py`: rules, persistence, failed writes, and terminal workflow.

## Tests

```bash
python -m unittest discover -s tests -v
```

GitHub Actions runs the tests on Python 3.10 and 3.12.

## Limitations

Single-user, single-process application. No database, authentication, stock movement history or web API yet. Do not run two instances against the same JSON file. Keep backups of your data. Files under data/ are excluded from Git.

## Next steps

- Product identifiers and movement history.
- SQLite persistence.
- A web API and interface after practicing the fundamentals.

## Learning notes

The key concepts are functions, dictionaries, loops, conditionals, exceptions, file operations, JSON and automated tests. Be prepared to explain why each validation exists and how failed saves are handled.

[Portfolio](https://oliveraraujo.github.io/portifolio/) · [GitHub](https://github.com/OliverAraujo)
