def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
S = 0
for i in range(1, 6):
    S += factorial(i)


print("S = ",S)
