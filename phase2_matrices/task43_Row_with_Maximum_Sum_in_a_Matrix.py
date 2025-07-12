def row_sums(matrix):
    row_sums_list = []
    for i in range(len(matrix)):
        row_sum = sum(matrix[i])
        print(f"Sum of row {i + 1}: {row_sum}")
        row_sums_list.append(row_sum)
    
    max_sum = max(row_sums_list)
    max_index = row_sums_list.index(max_sum)
    print("\nRow", max_index + 1, "has the maximum sum =", max_sum)
    print("Row:", matrix[max_index])

n = int(input("Enter the number of rows: "))
m = int(input("Enter the number of columns: "))
matrix = []
for i in range(n):
    row = []
    for j in range(m):
        element = int(input(f"A[{i+1}][{j+1}]: "))
        row.append(element)
    matrix.append(row)

row_sums(matrix)
