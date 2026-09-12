password = input("Enter a password to evaluate: ")

#keep track of checks passed bruh
length_ok = len(password) >= 8
has_uppercase = False
has_lowercase = False
has_digit = False
has_special = False

#special characters whatever you want, just put it down bruh
special_chars = "!@#$%^&*()_+=-[]|?/.,<>"

#loop through every char on the password and check if it meets the requirements bruh cmon man
for char in password:
    if char.isupper():
        has_uppercase = True
    elif char.islower():
        has_lowercase = True
    elif char.isdigit():
        has_digit = True
    elif char in special_chars:
        has_special = True

#just count how many fucking requirements the password written has met or just pack it up gng
requirements_met = sum([length_ok, has_uppercase, has_lowercase, has_digit, has_special])

#now evalute the fuck based on the fucking score dawg
print("\n-- password evaluation result --")
if requirements_met == 5:
    print(" dang bruh password strong like pullout game")
elif requirements_met == 3:
    print("bruh wtf cant u built sumthing stronger than a weak ass password")
else:
    print("pack it up gng u aint made for ts")