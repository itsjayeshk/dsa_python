n = int(input("Enter the number of rows and columns: "))
matrix = []
for i in range(n):
    row = []
    for j in range(n):
        element = int(input(f"A[{i+1}][{j+1}]: "))
        row.append(element)
    matrix.append(row)

primary_sum = 0
for i in range(n):
    primary_sum = primary_sum + matrix[i][i]

sec_sum = 0
for i in range(n):
    sec_sum = sec_sum + matrix[i][n-1-i]

print("Sum of primary diagonal: " ,primary_sum)
print("Sum of secondary diagonal: " ,sec_sum)