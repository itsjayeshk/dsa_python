n = int(input("Enter the number of rows and columns: "))
matrix = []
for i in range(n):
    row = []
    for j in range(n):
        element = int(input(f"A[{i+1}][{j+1}]: "))
        row.append(element)
    matrix.append(row)

is_symmetric = True  

for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i]:
            is_symmetric = False
            break
    if not is_symmetric:
        break

if is_symmetric:
    print("✅ It is a symmetric matrix")
else:
    print("❌ It is not a symmetric matrix")
