n = int(input("Enter the number of elements: "))
arr = []

for i in range(n):
    element = int(input("Enter an element: "))
    arr.append(element)

even = 0
odd = 0

for num in arr:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Number of even numbers:", even)
print("Number of odd numbers:", odd)