
# MATRICES

# Using Functions
"""import numpy as np

arr1 = np.array([[1, 2], [4, 5]])
arr2 = np.array([[6, 5], [3, 2]])

print("Array 1")
print(arr1)

print("Array 2")
print(arr2)

print("Addition")
print(np.add(arr1, arr2))

print("Subtraction")
print(np.subtract(arr1, arr2))

print("Multiplication")
print(np.dot(arr1, arr2))

print("Transpose")
print(np.transpose(arr1))
print(np.transpose(arr2)) """


# MATRIX 1
A = []

R = int(input("Enter the range for order of the First MATRIX (NxN) - "))

print("Enter the elements of matrix ")
for i in range(R):
    row = []
    for j in range(R):
        row.append(int(input()))
    A.append(row)

# Print in Matrix form
for i in range(R):
    for j in range(R):
        print(A[i][j], end=" ")
    print()

# MATRIX 2

B = []
R = int(input("Enter the range for order of the Second MATRIX (NxN) - "))
for i in range(R):
    row = []
    for j in range(R):
        row.append(int(input()))
    B.append(row)

for i in range(R):
    for j in range(R):
        print(B[i][j], end=" ")
    print()

result = [[0 for j in range(R)] for i in range(R)]
#print(result)

# Multiplication MATRIX of A and B

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j] = result[i][j] + A[i][k] * B[k][j]
print("Multiplication is")
for num in result:
    print(num)

# Addition of MATRIX A & B

for i in range(R):
    for j in range(len(A[0])):
        result[i][j] = A[i][j] + B[i][j]
print("The ADDITION is")
for num in result:
    print(num)

# Subtraction of MATRIX A from B

for i in range(R):
    for j in range(R):
        result[i][j] = A[i][j] - B[i][j]
print("The SUBTRACTION is")
for num in result:
    print(num)

# Transpose of A and B

for i in range(R):
    for j in range(R):
        result[i][j] = A[j][i]
print("Transpose of A is")
for num in result:
    print(num)


for i in range(R):
    for j in range(R):
        result[i][j] = B[j][i]
print("Transpose of B is")
for num in result:
    print(num)



