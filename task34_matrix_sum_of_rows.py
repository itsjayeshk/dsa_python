def row_sums(matrix):
    for i in range(len(matrix)):
        row_sum = sum(matrix[i])
        print(f"Sum of row {i + 1}: {row_sum}")

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

row_sums(matrix)
