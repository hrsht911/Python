# Define a custom exception by inheriting from Python's built-in Exception class
class InsufficientStockError(Exception):
    """Raised when an item's requested quantity exceeds available inventory."""
    pass


def manage_inventory():
    # 1. Dictionary storing item names and their stock quantities
    inventory = {
        "sword": 5,
        "potion": 12,
        "shield": 2
    }

    print("Current Inventory:")
    # 2. For loop to iterate through dictionary keys and values
    for item, stock in inventory.items():
        print(f" - {item}: {stock} available")

    print("\nProcessing transactions...")
    
    # 3. While loop to handle multiple checkout requests
    active = True
    while active:
        target_item = input("\nEnter item to buy (or type 'quit' to exit): ").strip().lower()

        if target_item == 'quit':
            active = False
            print("Exiting inventory system.")
            continue

        # 4. If-Else conditional to check dictionary keys
        if target_item in inventory:
            try:
                quantity_str = input(f"How many {target_item}s would you like? ")
                quantity = int(quantity_str)

                # 5. Raising a custom error if condition fails
                if quantity > inventory[target_item]:
                    raise InsufficientStockError(
                        f"Error: Tried to buy {quantity} {target_item}(s), but only {inventory[target_item]} are left."
                    )

                # Update dictionary value if successful
                inventory[target_item] -= quantity
                print(f"Success! Remaining {target_item}: {inventory[target_item]}")

            except InsufficientStockError as e:
                # Catch the custom error
                print(f"[Custom Exception Caught]: {e}")
            except ValueError:
                # Handle non-integer inputs
                print("Invalid input. Please enter a valid number.")
        else:
            print(f"'{target_item}' does not exist in the inventory.")


if __name__ == "__main__":
    manage_inventory()