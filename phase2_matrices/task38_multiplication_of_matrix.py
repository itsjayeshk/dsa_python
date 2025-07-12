
n = int(input("Enter number of rows for Matrix A: "))
m = int(input("Enter number of columns for Matrix A: "))

matrix1 = []
print("\nEnter elements for Matrix A:")
for i in range(n):
    row = []
    for j in range(m):
        element = int(input(f"A[{i+1}][{j+1}]: "))
        row.append(element)
    matrix1.append(row)

p = int(input("\nEnter number of columns for Matrix B: "))


matrix2 = []
print("\nEnter elements for Matrix B:")
for i in range(m):  
    row = []
    for j in range(p):
        element = int(input(f"B[{i+1}][{j+1}]: "))
        row.append(element)
    matrix2.append(row)


result = []
for i in range(n):
    new_row = []
    for j in range(p):
        cell_sum = 0
        for k in range(m):
            cell_sum += matrix1[i][k] * matrix2[k][j]
        new_row.append(cell_sum)
    result.append(new_row)


print("\nMatrix A:")
for row in matrix1:
    print(row)

print("\nMatrix B:")
for row in matrix2:
    print(row)

print("\nResultant Matrix (A x B):")
for row in result:
    print(row)

