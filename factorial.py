def factorial(i):
    result = i

    for j in range(i - 1, 1, -1):
        result = result * j

    return result

x = 6
print("3! =", factorial(3))
print("5! =", factorial(5))
