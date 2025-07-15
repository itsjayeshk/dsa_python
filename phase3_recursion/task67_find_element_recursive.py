def find_elem(n, arr, index=0):
    if index == len(arr):
        return False
    if arr[index] == n:
        return True
    return find_elem(n, arr, index + 1)


arr = []
n = int(input("Enter the number of elements: "))
for i in range(n):
    element = int(input("Enter element: "))
    arr.append(element)

num = int(input("Enter the element you want to search: "))


if find_elem(num, arr):
    print(f"✅ Element {num} is present in the array.")
else:
    print(f"❌ Element {num} is not present in the array.")
