def print_array(arr, index = 0):
    if index == len(arr):
        return 0
    else:
        print(arr[index])
        return print_array(arr, index + 1)
arr = []
n = int(input("Enter the number of elements: "))
for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    arr.append(element)
print_array(arr)    

    
    # base case: stop when index == len(arr)
    # print current element
    # recursively call for next index
