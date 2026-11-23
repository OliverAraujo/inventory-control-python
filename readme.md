# 📦 Inventory Control with Python

A terminal-based inventory management application built as a learning project to practice Python fundamentals.

The application allows users to register products with an initial stock quantity, record incoming and outgoing stock, and view the current inventory.

## Features

- Register products with an initial stock quantity.
- Prevent empty or duplicate product names.
- Record incoming stock.
- Record outgoing stock.
- Prevent withdrawals exceeding available stock.
- Display all products and their current quantities.
- Handle invalid menu options and quantity inputs.

Product names are converted to lowercase and trimmed of leading and trailing spaces. For example, `Mouse` and `mouse` refer to the same product.

## Technologies

- Python 3
- Git and GitHub for version control

No external Python libraries are required.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/OliverAraujo/inventory-control-python.git
```

### 2. Open the project folder

```bash
cd inventory-control-python
```

### 3. Run the application

```bash
python main.py
```

On Windows, you can also use:

```bash
py main.py
```

On systems where Python 3 uses a separate command:

```bash
python3 main.py
```

## How to Use

When prompted, enter `Y` to access the system.

```text
--- INVENTORY CONTROL ---
1 - Register a product
2 - Record incoming stock
3 - Record outgoing stock
4 - View inventory
5 - Exit
```

| Option | Description |
|--------|-------------|
| 1 | Register a product and its initial quantity |
| 2 | Add units to a registered product |
| 3 | Remove units from a registered product |
| 4 | Display products and stock quantities |
| 5 | Close the application |

The menu reappears after each operation so you can perform another action.

### Example Workflow

1. Register `mouse` with an initial quantity of `10`.
2. Add `5` units using option `2`.
3. Remove `3` units using option `3`.
4. Select option `4` to view the result:

```text
--- CURRENT INVENTORY ---
- mouse: 12 unit(s)
```

## Validation Rules

- Product names cannot be empty.
- Products cannot be registered more than once under the same normalized name.
- Initial stock must be a whole number greater than or equal to zero.
- Incoming and outgoing quantities must be positive whole numbers.
- Outgoing quantities cannot exceed available stock.
- Invalid quantity inputs display an error message and return to the menu.

## Data Storage

Products are stored in a Python dictionary, where each product name is associated with its quantity:

```python
products = {
    "mouse": 12,
    "keyboard": 5
}
```

**Data is stored only in memory and is lost when the application closes.**

This version does not use a database or save data to files. The initial Y/N prompt is a confirmation to enter the program, not a login or authentication system.

## Learning Goals

This project practices:

- Variables and dictionaries.
- User input and output with `input()` and `print()`.
- Conditional statements with `if`, `elif`, and `else`.
- Loops with `while` and `for`.
- Dictionary operations and iteration with `.items()`.
- String methods such as `.strip()`, `.lower()`, and `.upper()`.
- Integer conversion with `int()`.
- Error handling with `try` and `except ValueError`.
- String formatting with f-strings.
- Input validation and basic inventory rules.

## Future Improvements

- [ ] Organize the code into reusable functions.
- [ ] Add automated tests.
- [ ] Integrate a database to persist inventory data.
- [ ] Create a graphical user interface.
- [ ] Add unique product identifiers.
- [ ] Record stock movement history.

## Author

**Oliver Araújo**

Graduate in Systems Analysis and Development, currently learning Python with a focus on backend development.

- [GitHub](https://github.com/OliverAraujo)
- [Portfolio](https://oliveraraujo.github.io/portifolio/)