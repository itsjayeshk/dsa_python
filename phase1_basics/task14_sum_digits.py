num = int(input("Enter a number: "))
total = 0
while num > 0:
    dig = num % 10
    total = total + dig
    num = num // 10

print("Total of digits", total)