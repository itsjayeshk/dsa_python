n = int(input("Enter the number of elements: "))
arr = []

for i in range(n):
    element = int(input("Enter an element: "))
    arr.append(element)

positive = negative = zero = 0

for num in arr:
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    else:
        zero += 1

print("Number of positive numbers:", positive)
print("Number of negative numbers:", negative)
print("Number of zero numbers:", zero)