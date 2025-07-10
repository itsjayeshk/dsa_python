def gcd_recursive(a, b):
    if b == 0:
        return a
    return gcd_recursive(b, a % b)

def lcm_of_number(a, b):
    return abs(a * b) // gcd_recursive(a, b)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("LCM:", lcm_of_number(num1, num2))
