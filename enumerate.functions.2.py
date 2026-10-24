class InvalidSelectionError(Exception):
    pass

apps = ["Instagram", "Chrome", "Whatsapp", "Pinterest"]

for index, app in enumerate(apps, start=1):
    print(f"{index}.{app}")

choice = int(input("Pick a Number:"))

try:
    if choice < 1 or choice > len(apps):
     raise InvalidSelectionError("Invalid choice number!")
    print(f"Opened: {apps[choice - 1]}")
except InvalidSelectionError as e:
    print(e)