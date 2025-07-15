def binary_search(arr, low, high, target):
    if low > high:
        return -1  # base case: element not found

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif target < arr[mid]:
        return binary_search(arr, low, mid - 1, target)
    else:
        return binary_search(arr, mid + 1, high, target)

# Input
arr = []
n = int(input("Enter the number of elements: "))
for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    arr.append(element)

arr.sort()
print("Sorted array:", arr)

target = int(input("Enter the element to search: "))
result = binary_search(arr, 0, len(arr) - 1, target)

if result != -1:
    print(f"✅ Element found at index {result}")
else:
    print("❌ Element not found in array")


    