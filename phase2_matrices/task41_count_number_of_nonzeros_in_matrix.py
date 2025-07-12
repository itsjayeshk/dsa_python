n = int(input("Enter the number of rows in matrix: "))
m = int(input("Enter the number of columns in matrix: "))
matrix = []
for i in range(n):
    row = []
    for j in range(m):
        element = int(input(f"Enter the A[{i+1}][{j+1}]: "))
        row.append(element)
    matrix.append(row)

total = m * n
zero = 0
nonzero = 0
for i in range(n):
   for j in range(m):
      if matrix[i][j] == 0:
         zero = zero + 1
      else:
         nonzero = nonzero + 1

print("Number of zeros: " ,zero)
print("Number of non zeros: " ,nonzero)

 
                