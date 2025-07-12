num = int(input("Enter a number: "))
reverse = 0
num1 = num

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if num1 == reverse:
    print("The number is palindrome")
else:
    print("It is not")