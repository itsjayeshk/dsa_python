def pow(a ,b):
    if b == 0:
        return 1
    else:
        return a * pow(a, b-1)

x = int(input("Enter the base: "))
y = int(input("Enter the exponent: "))   
print("Value is: " ,pow(x ,y))

