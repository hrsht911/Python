def restaurant_order_system():
    # 1. Dictionary storing menu items and their prices
    menu = {
        "Cheeseburger": 8.99,
        "Pepperoni Pizza": 12.50,
        "Caesar Salad": 6.75,
        "French Fries": 3.00,
        "Soft Drink": 2.50,
    }

    cart = {}

    print("========================================")
    print("      WELCOME TO PYTHON BISTRO!         ")
    print("========================================")

    while True:
        print("\n--- Menu ---")
        menu_items = list(menu.keys())

        # Using enumerate() to display the menu with numbers starting from 1
        for index, item in enumerate(menu_items, start=1):
            price = menu[item]
            print(f"{index}. {item:<18} - ${price:.2f}")

        print(f"{len(menu_items) + 1}. Checkout & Print Bill")

        # Get user choice
        choice = input(
            f"\nSelect an item number (1-{len(menu_items) + 1}): "
        ).strip()

        if not choice.isdigit():
            print("Invalid input. Please enter a valid number.")
            continue

        choice_num = int(choice)

        # Check if user wants to checkout
        if choice_num == len(menu_items) + 1:
            break

        # Validate menu selection
        if 1 <= choice_num <= len(menu_items):
            selected_item = menu_items[choice_num - 1]
            qty_input = input(f"Enter quantity for {selected_item}: ").strip()

            if qty_input.isdigit() and int(qty_input) > 0:
                qty = int(qty_input)
                # Update the cart dictionary
                cart[selected_item] = cart.get(selected_item, 0) + qty
                print(
                    f"-> Added {qty}x {selected_item}(s) to your order cart."
                )
            else:
                print("Please enter a valid positive number for quantity.")
        else:
            print("Selection out of range. Please choose a valid number.")

    # 3. Generate Bill using dictionaries and enumerate()
    print("\n" + "=" * 40)
    print("              FINAL BILL                ")
    print("========================================")

    if not cart:
        print("No items ordered. Hope to see you next time!")
    else:
        total_amount = 0
        # Using enumerate() again to format the final bill receipt
        for i, (item, qty) in enumerate(cart.items(), start=1):
            item_total = menu[item] * qty
            total_amount += item_total
            print(
                f"{i}. {item:<15} x {qty}  = ${item_total:>6.2f} (${menu[item]:.2f} ea)"
            )

        print("-" * 40)
        print(f"TOTAL DUE: ${total_amount:.2f}")
        print("========================================")
        print("    Thank you for dining with us!       ")


if __name__ == "__main__":
    restaurant_order_system()