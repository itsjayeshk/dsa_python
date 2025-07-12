n = int(input("Enter the number of elements: "))
arr = []

for i in range(n):
    element = int(input("Enter an element: "))
    arr.append(element)

average = sum(arr) / n
print("Average:", average)