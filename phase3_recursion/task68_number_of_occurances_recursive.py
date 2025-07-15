def find_elem(n, arr, index=0, indices=None):
    if indices is None:
        indices = []

    if index == len(arr):
        return indices

    if arr[index] == n:
        indices.append(index)

    return find_elem(n, arr, index + 1, indices)



arr = []
n = int(input("Enter the number of elements: "))
for i in range(n):
    element = int(input("Enter element: "))
    arr.append(element)

num = int(input("Enter the element you want to search: "))


result = find_elem(num, arr)
if result:
    print(f"✅ Element {num} found at indices:", result)
else:
    print(f"❌ Element {num} not found in the array.")

