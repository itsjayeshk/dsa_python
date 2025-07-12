num = int(input("Enter a number: "))
largest = 0
while num > 0:
    dig = num % 10
    num = num // 10
    if dig > largest:
        largest = dig

print("Largest digit:", largest)