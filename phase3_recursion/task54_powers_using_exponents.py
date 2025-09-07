def power(base, exp):
    if exp == 0:  
        return 1
    return base * power(base, exp - 1) 
b = int(input("Enter base: "))
e = int(input("Enter exponent: "))
print(f"{b}^{e} =", power(b, e))
