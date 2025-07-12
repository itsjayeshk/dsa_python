def print_n(n):
    if n == 0:
        return
    print(n, end=" ")      
    print_n(n - 1)

num = int(input("Enter N: "))
print_n(num)
