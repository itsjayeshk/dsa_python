def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

n = int(input("Enter the number whose factorial you want: "))
print("Factorial is", factorial(n))
