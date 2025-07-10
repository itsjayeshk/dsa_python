n = int(input("Enter the number of elements: "))
arr = [] 

for i in range(n):
    element = int(input("Enter an element: "))
    arr.append(element)

min_element = min(arr)
print("Minimum element:", min_element)