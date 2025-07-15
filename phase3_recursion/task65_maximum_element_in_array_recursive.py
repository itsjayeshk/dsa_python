def max_array(arr, index=0, current_max=None):
    if current_max is None:
        current_max = arr[0]
    
    if index == len(arr):
        return current_max
    
    if arr[index] > current_max:
        current_max = arr[index]
    
    return max_array(arr, index + 1, current_max)

# Input
arr = []
n = int(input("Enter the number of elements: "))
for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    arr.append(element)

print("Maximum element:", max_array(arr))

 