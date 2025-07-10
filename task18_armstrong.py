num = int(input("Enter a number: "))
num1 = num
digits = 0
sum = 0
temp = num

while temp > 0:
    digits += 1
    temp //= 10

temp = num
while temp > 0:
    dig = temp % 10
    sum += pow(dig, digits)
    temp //= 10

if num1 == sum:
    print("Armstrong number")
else:
    print("Not armstrong")