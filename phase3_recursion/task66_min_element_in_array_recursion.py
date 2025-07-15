def min_array(arr, index=0, current_min=None):
    if current_min is None:
        current_min = arr[0]
    
    if index == len(arr):
        return current_min
    
    if arr[index] < current_min:
        current_min = arr[index]
    
    return min_array(arr, index + 1, current_min)

# Input
arr = []
n = int(input("Enter the number of elements: "))
for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    arr.append(element)

print("Minimum element:", min_array(arr))