"""Terminal interface. Run with python main.py."""
from inventory import register_product, record_entry, record_issue
from storage import DEFAULT_PATH, load_inventory, save_inventory

MENU = """
--- INVENTORY CONTROL ---
1 - Register a product
2 - Record incoming stock
3 - Record outgoing stock
4 - View inventory
5 - Exit"""


def show_inventory(products):
    if not products:
        print("No products registered.")
        return
    print("\n--- CURRENT INVENTORY ---")
    for name, quantity in sorted(products.items()):
        print(f"- {name}: {quantity} unit(s)")


def main(path=DEFAULT_PATH):
    print("Welcome to the inventory control system!")
    try:
        products = load_inventory(path)
    except (OSError, ValueError) as error:
        print(f"Cannot load inventory: {error}")
        print("Your existing file has not been changed. Check it before restarting.")
        return 1

    try:
        if input("Would you like to access the system? (Y/N): ").strip().upper() != "Y":
            print("Access canceled.")
            return 0
        while True:
            print(MENU)
            option = input("Choose an option: ").strip()
            if option == "5":
                print("System closed. Goodbye!")
                return 0
            if option == "4":
                show_inventory(products)
                continue
            operations = {"1": register_product, "2": record_entry, "3": record_issue}
            if option not in operations:
                print("Invalid option! Choose a number from 1 to 5.")
                continue
            name = input("Enter the product name: ")
            try:
                quantity = int(input("Enter the quantity: "))
                # Work on a copy: a failed save must not change the active stock.
                updated = products.copy()
                operations[option](updated, name, quantity)
                save_inventory(updated, path)
            except ValueError as error:
                print(f"Invalid operation: {error}")
            except OSError as error:
                print(f"Could not save inventory: {error}. Operation canceled.")
            else:
                products = updated
                print("Operation saved successfully.")
                show_inventory(products)
    except (EOFError, KeyboardInterrupt):
        print("\nSystem closed. Completed operations are already saved.")
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
