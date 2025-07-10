n = int(input("Enter the number of elements: "))
arr = [] 

for i in range(n):
    element = int(input("Enter an element: "))
    arr.append(element)

max_element = max(arr)
print("Maximum element:", max_element)