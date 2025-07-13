def rec_sum(n):
    if n == 0:
        return 0
    else:
        return n + rec_sum(n - 1)

n = int(input("Enter the number whose sum you want: "))
print("Sum is: " ,rec_sum(n))