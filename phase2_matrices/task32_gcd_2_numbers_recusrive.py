def gcd_recursive(a, b):
    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Highest GCD:", gcd_recursive(num1, num2))
