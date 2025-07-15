def count_digits(n):
    if abs(n) < 10:
        return 1
    else:
        return 1 + count_digits(abs(n) // 10)

num = int(input("Enter the number to count digits: "))
print("Number of digits:", count_digits(num))
