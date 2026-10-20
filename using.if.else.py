# Students Grade Evaluator:-

title = "Students Grade Evaluator"
print(title)


#1. Ask the user his/her aggregate marks 
marks = int(input("Enter your overall marks here (0-100): "))

#2.Using if, else, elif statements to evaluate the user grades.
if marks >= 90:
    print("Your grade:A+")
elif marks >=80:
    print("Your grade:A")
elif marks >=70:
    print("Your Grade:B+")
elif marks >=60:
    print("Your Grade:B")           
elif marks >=50:
    print("Your Grade:C+")
elif marks >=40:
    print("Your Grade:C")
elif marks >= 35:
    print("Your Grade:D")
else:
    print("You Failed! Better Luck Next Time!")