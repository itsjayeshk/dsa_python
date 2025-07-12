n = int(input("Enter the number of rows and columns: "))
matrix = []
for i in range(n):
    row = []
    for j in range(n):
        element = int(input(f"A[{i+1}][{j+1}]: "))
        row.append(element)
    matrix.append(row)

is_lower_triangular = True

for i in range(n):
    for j in range(n):
        if i < j:
            if matrix[i][j] != 0:
                is_lower_triangular = False
                break
        


        
    if not is_lower_triangular:
        break

if is_lower_triangular:
    print("✅ It is a lower triangular matrix")
else:
    print("❌ It is not a lower triangular matrix")