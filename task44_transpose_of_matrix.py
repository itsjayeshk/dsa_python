n = int(input("Enter the number of rows: "))
m = int(input("Enter the number of columns: "))
matrix = []
for i in range(n):
    row = []
    for j in range(m):
        element = int(input(f"A[{i+1}][{j+1}]: "))
        row.append(element)
    matrix.append(row)

transpose = []
for j in range(m):  
    new_row = []
    for i in range(n):  
        new_row.append(matrix[i][j])
    transpose.append(new_row)

print("Transpose: ")
for row in transpose:
    print(row)