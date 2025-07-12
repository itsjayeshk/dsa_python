def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

num = int(input("Enter the number: "))
original_num = num
total = 0

while num > 0:
    dig = num % 10
    total += factorial(dig)
    num = num // 10

if total == original_num:
    print("Number is a Strong Number")
else:
    print("It is not a Strong Number")
