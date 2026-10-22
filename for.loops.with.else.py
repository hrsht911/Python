attempts = 3

while attempts > 0:
    password = input("Enter Password:")
    if password == "1234567890":
        print("Access Granted!")
        break
    attempts -=1
else:
    print("Account Locked.Too Many Failed Attempts!")