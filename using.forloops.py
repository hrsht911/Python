#Multiplication table generator using for loops:-
given_number = int(input("Enter your number here:"))

for i in range(1, 11):
    result = given_number * i
    print(f"{given_number} X {i} = {result}")