n = int(input("Enter the number of rows and columns for matrix: "))

matrix = []
print("Enter the elements of matrix:")
for i in range(n):
    row = []
    for j in range(n):
        element = int(input(f"A[{i+1}][{j+1}]: "))
        row.append(element)
    matrix.append(row)

top = 0
bottom = n - 1
left = 0
right = n - 1

print("\nSpiral order:")
while top <= bottom and left <= right:

    for i in range(left, right + 1):
        print(matrix[top][i], end=" ")
    top = top + 1

    for i in range(top, bottom + 1):
        print(matrix[i][right], end=" ")
    right = right - 1

    if top <= bottom:
        for i in range(right, left - 1, -1):
            print(matrix[bottom][i], end=" ")
        bottom = bottom - 1

    if left <= right:
        for i in range(bottom, top - 1, -1):
            print(matrix[i][left], end=" ")
        left = left + 1
