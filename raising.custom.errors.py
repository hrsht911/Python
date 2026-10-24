class InvalidPasswordError(Exception):
    pass


password = input("Enter Your password:")
try:
    if password == "wrong_password1234":
        print("Access Granted!")

    elif password != "wrong_password1234":
     raise InvalidPasswordError("The Password is Incorrect!")
except InvalidPasswordError as e:
    print(e)




    #here i have created a custom error 