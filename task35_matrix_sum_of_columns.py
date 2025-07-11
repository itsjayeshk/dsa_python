def column_sums(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    for j in range(cols):
        col_sum = 0
        for i in range(rows):
            col_sum += matrix[i][j]
        print(f"Sum of column {j + 1}: {col_sum}")

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

column_sums(matrix)
