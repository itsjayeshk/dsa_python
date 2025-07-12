n = int(input("Enter the number of elements: "))
arr = []

for i in range(n):
    element = int(input("Enter an element: "))
    arr.append(element)

print("Reversed array:")
for i in range(n - 1, -1, -1):
    print(arr[i])