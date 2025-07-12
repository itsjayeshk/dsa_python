n = int(input("Enter the number of rows and columns: "))
matrix = []
for i in range(n):
    row = []
    for j in range(n):
        element = int(input(f"A[{i+1}][{j+1}]: "))
        row.append(element)
    matrix.append(row)

is_identity = True

for i in range(n):
    for j in range(n):
        if i == j:
            if matrix[i][j] != 1:
                is_identity = False
        else:
            if matrix[i][j] != 0:
                is_identity = False

if is_identity:
    print("✅ It is an identity matrix")
else:
    print("❌ It is not an identity matrix")
