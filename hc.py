def f(x):
    return -(x-5)**2+25
def hill_climbing(start):
    current=start
    while True:
        Left = current-1
        Right = current+1
        if f(Left) > f(current):
            Next_state= Left
        elif f(Right) > f(current):
            Next_state= Right
        else:
            break
        current = Next_state
    return current, f(current)
Start= 0
Solution, Value = hill_climbing(Start)

print("Starting point",Start)
print("Best solution",Solution)
print("Maximum value",Value)