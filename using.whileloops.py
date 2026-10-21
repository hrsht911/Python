#making a secret password door using while loops:-

#1.setting up the password in memory
password = "helloworld123456"

#2.asking the user to guess/enter the password
user_input = input("enter your password here:")

while user_input != password:
    print("Incorrect password! Access denied!!")
    user_input = input("Enter Your Password Here:")

    print("Password Correct!Access Granted!!")