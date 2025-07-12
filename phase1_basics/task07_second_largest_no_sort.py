n = int(input("Enter the number of elements: "))
arr = [] 

for i in range(n):
    element = int(input("Enter an element: "))
    arr.append(element)

first = second = float('-inf')

for num in arr:
    if num > first:
        second = first
        first = num
    elif num > second and num != first:
        second = num

print("Second largest element is:", second)