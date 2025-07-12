def column_sums(matrix):
    columns_sum_list = []
    rows = len(matrix)
    cols = len(matrix[0])
    
    for j in range(cols):
        col_sum = 0
        for i in range(rows):
            col_sum += matrix[i][j]
        print(f"Sum of column {j + 1}: {col_sum}")
        columns_sum_list.append(col_sum)
    
    max_sum = max(columns_sum_list)
    max_index = columns_sum_list.index(max_sum)
    
    print("\nColumn", max_index + 1, "has the maximum sum =", max_sum)
    print("Column:", [matrix[i][max_index] for i in range(rows)])

n = int(input("Enter the number of rows: "))
m = int(input("Enter the number of columns: "))
matrix = []
for i in range(n):
    row = []
    for j in range(m):
        element = int(input(f"A[{i+1}][{j+1}]: "))
        row.append(element)
    matrix.append(row)

column_sums(matrix)
