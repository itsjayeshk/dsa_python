n = int(input("Enter the number of elements: "))
arr = []

for i in range(n):
    element = int(input("Enter an element: "))
    arr.append(element)

for i in range(n):
    sum = 0
    for j in range(i, n):
        sum += arr[j]
        print(sum, end=" ")
    print()