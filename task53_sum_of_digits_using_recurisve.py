def sum_of_n(n):
    if n == 0:
        return 0
    elif n != 0:
        return (n % 10) + sum_of_n(n//10)

n = int(input("Enter the number whose digits sum you want: "))
print("Sum of digits is: " ,sum_of_n(n))