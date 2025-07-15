def rever(n, arr, index=0):
    if index == n:
        return
    rever(n, arr, index + 1)
    print(arr[index], end=" ")

arr1 = []
num = int(input("Enter the number of elements: "))
for i in range(num):
    element = int(input("Enter element: "))
    arr1.append(element)

print("Reverse order: ", end="")
rever(num, arr1)
