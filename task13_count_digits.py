num = int(input("Enter a number: "))
digit = 0
while num > 0:
    dig = num % 10
    digit = digit + 1
    num = num // 10

print("Number of digits", digit)