n = int(input("Enter number of rows: "))
m = int(input("Enter number of columns: "))

matrix1 = []
matrix2 = []

print("\nEnter elements for Matrix 1:")
for i in range(n):
    row = []
    for j in range(m):
        element = int(input(f"Matrix1 [{i+1}][{j+1}]: "))
        row.append(element)
    matrix1.append(row)

print("\nEnter elements for Matrix 2:")
for i in range(n):
    row = []
    for j in range(m):
        element = int(input(f"Matrix2 [{i+1}][{j+1}]: "))
        row.append(element)
    matrix2.append(row)

matrix3 = []
for i in range(n):  
    new_row = []
    for j in range(m): 
        new_row.append(matrix1[i][j] + matrix2[i][j])
    matrix3.append(new_row)

print("\nMatrix 1:")
for row in matrix1:
    print(row)

print("\nMatrix 2:")
for row in matrix2:
    print(row)

print("\nAdded Matrix:")
for row in matrix3:
    print(row)
