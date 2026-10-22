user_memory = {}

print("|---Build Your Profile---|")

username_input = input("Enter your Username here:")
level_input = int(input("Enter your Level here:"))
class_input = input("Enter Your class here:")
life_input = input("Enter your life stat here:")

user_memory["Username"] = username_input
user_memory["Level"] = level_input
user_memory["Class"] = class_input
user_memory["Life Stat"] = life_input

print("---Saved Memory Dictionary---")
print(user_memory)