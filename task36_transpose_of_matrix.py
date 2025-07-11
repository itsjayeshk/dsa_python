n = int(input("Enter number of rows: "))
m = int(input("Enter number of columns: "))

matrix = []

for i in range(n):
    row = []
    print(f"\nEnter elements for row {i + 1}:")
    for j in range(m):
        element = int(input(f"Element [{i+1}][{j+1}]: "))
        row.append(element)
    matrix.append(row)

transpose = []

for j in range(m):  # columns
    new_row = []
    for i in range(n):  # rows
        new_row.append(matrix[i][j])
    transpose.append(new_row)

print("\nOriginal Matrix:")
for row in matrix:
    print(row)

print("\nTransposed Matrix:")
for row in transpose:
    print(row)
