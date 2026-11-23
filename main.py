# Inventory Control System
# Data is stored in memory while the program is running.

products = {}

print("Welcome to the inventory control system!")

access = input(
    "Would you like to access the system? (Y/N): "
).strip().upper()

if access == "Y":
    option = ""

    while option != "5":
        print("\n--- INVENTORY CONTROL ---")
        print("1 - Register a product")
        print("2 - Record incoming stock")
        print("3 - Record outgoing stock")
        print("4 - View inventory")
        print("5 - Exit")

        option = input("Choose an option: ").strip()

        # Register a product with its initial stock quantity.
        if option == "1":
            name = input("Enter the product name: ").strip().lower()

            if name == "":
                print("The product name cannot be empty.")

            elif name in products:
                print("This product is already registered.")

            else:
                try:
                    quantity = int(
                        input("Enter the initial stock quantity: ")
                    )

                    if quantity < 0:
                        print("The stock quantity cannot be negative.")

                    else:
                        products[name] = quantity
                        print(f"Product '{name}' registered successfully!")
                        print(f"Initial stock: {quantity} unit(s).")

                except ValueError:
                    print("Invalid quantity. Enter a whole number.")

        # Add units to an existing product.
        elif option == "2":
            name = input("Enter the product name: ").strip().lower()

            if name not in products:
                print("Product not found. Register it first.")

            else:
                try:
                    quantity = int(
                        input("Enter the quantity to add: ")
                    )

                    if quantity <= 0:
                        print("The quantity must be greater than zero.")

                    else:
                        products[name] += quantity
                        print(f"Added {quantity} unit(s) to '{name}'.")
                        print(f"Current stock: {products[name]} unit(s).")

                except ValueError:
                    print("Invalid quantity. Enter a whole number.")

        # Remove units without allowing negative stock.
        elif option == "3":
            name = input("Enter the product name: ").strip().lower()

            if name not in products:
                print("Product not found.")

            else:
                try:
                    quantity = int(
                        input("Enter the quantity to remove: ")
                    )

                    if quantity <= 0:
                        print("The quantity must be greater than zero.")

                    elif quantity > products[name]:
                        print("Insufficient stock.")
                        print(f"Available stock: {products[name]} unit(s).")

                    else:
                        products[name] -= quantity
                        print(f"Removed {quantity} unit(s) from '{name}'.")
                        print(f"Current stock: {products[name]} unit(s).")

                except ValueError:
                    print("Invalid quantity. Enter a whole number.")

        # Display all products and their stock quantities.
        elif option == "4":
            if products:
                print("\n--- CURRENT INVENTORY ---")

                for name, quantity in products.items():
                    print(f"- {name}: {quantity} unit(s)")

            else:
                print("No products registered.")

        # Exit the system.
        elif option == "5":
            print("System closed. Goodbye!")

        else:
            print("Invalid option! Choose a number from 1 to 5.")

else:
    print("Access canceled.")