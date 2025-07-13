def product1(n):
    if n == 0:
        return 1
    elif n % 10 == 0:
        return 0
    else:
        return (n % 10) * product1(n // 10)

n = int(input("Enter the number: "))
print("Product is:", product1(n))
