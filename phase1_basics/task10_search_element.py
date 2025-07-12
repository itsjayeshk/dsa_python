n = int(input("Enter the number of elements: "))
arr = []

for i in range(n):
    element = int(input("Enter an element: "))
    arr.append(element)

hi = int(input("Enter the number to search: "))
found = False

for i in range(n):
    if arr[i] == hi:
        print("Element found at index:", i)
        found = True
        break

if not found:
    print("Element not found")