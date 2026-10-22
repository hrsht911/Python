#factorial(5) = 5*4*3*2*1
#factorial(4) = 4*3*2*1
#factorial(3) = 3*2*1
#factorial(2) = 2*1
#factorial(1) = 1
#factorial(0) = 1

#factorial(n) = n * factorial(n-1)
def factorial(n):
  if(n ==0):
    return 1
  else:
    return n * factorial(n-1)

fact = int(input("Enter you factorial number:"))
print(factorial(fact))
