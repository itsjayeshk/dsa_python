num = int(input("Enter a number: "))
product = 1
while num > 0:
    dig = num % 10
    product = product * dig
    num = num // 10

print("Product of digits", product)