def sum_to_n(n):
    if n == 0:
        print("->Hit the bottom! Returning 0")
        return 0 
    print(f"Going down: n is {n}")
    result = n + sum_to_n(n - 1)
     
    print(F"Coming back up: for n = {n}, total is {result}")
    return result

print("Final Answer;", sum_to_n(3))