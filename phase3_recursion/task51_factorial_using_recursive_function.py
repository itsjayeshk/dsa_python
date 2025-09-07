def factorial(n):
    if n == 0 or n == 1: 
        return 1
    return n * factorial(n - 1)  
x = int(input("Enter a number: "))
print("Factorial of", x, "is:", factorial(x))
