n = int(input("Enter the number of rows in matrix: "))
m = int(input("Enter the number of columns in matrix: "))
matrix = []

for i in range(n):
    row = []
    for j in range(m):
        element = int(input(f"Enter the A[{i+1}][{j+1}]: "))
        row.append(element)
    matrix.append(row)

total = m * n
zero = 0
nonzero = 0

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0:
            zero += 1
        else:
            nonzero += 1

if zero > (total / 2):
    print("It is a sparse matrix")
else:
    print("It is not a sparse matrix")

print("Number of zero elements:", zero, "and nonzero elements:", nonzero)
