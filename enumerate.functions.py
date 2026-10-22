fruits = ["apple", "mango", "banana", "pears"]

print("---Fruit Vault---")
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}.{fruit}")

try:
    choice = int(input("\nPick a fruit of your choice:"))
    selected_fruit = fruit[choice - 1] if 0 <choice <= len(fruits) else None

    if selected_fruit:
        print(f"Loading up {selected_fruit}.")
    else:
        print("Could not be found")

except ValueError:
    print("Couldnt find anything")

