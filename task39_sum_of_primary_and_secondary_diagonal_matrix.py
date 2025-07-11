n = int(input("Enter the number of rows and columns for matrix: "))


matrix = []
print("Enter elements for Matrix: ")
for i in range(n):
    row = []
    for j in range(n):
        element = int(input(f"A[{i+1}][{j+1}]: "))
        row.append(element)
    matrix.append(row)

sum1 = 0
for i in range(n):
    sum1 = sum1 + matrix[i][i]

sum2 = 0
for i in range(n):
    sum2 = sum2 + matrix[i][n - 1 - i]

print("sum of secondary diagonal elements is: " ,sum2)     


print("sum of primary diagonal elements is: " ,sum1)        