def is_sort(arr, index=0):

    if index == len(arr) - 1:
        return True

    
    if arr[index] >= arr[index + 1]:
        return False

   
    return is_sort(arr, index + 1)


arr = []
n = int(input("Enter the number of elements in array: "))
for i in range(n):
    element = int(input("Enter the element: "))
    arr.append(element)

print("Array:", arr)
if is_sort(arr):
    print(" Array is strictly increasing (sorted)")
else:
    print(" Array is not sorted")



