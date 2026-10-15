import numpy as np

# Create matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("Matrix A:\n", A)
print("Matrix B:\n", B)

# Matrix operations
print("Addition:\n", A + B)
print("Multiplication:\n", np.dot(A, B))
print("Transpose of A:\n", A.T)
print("Determinant of A:", np.linalg.det(A))

# Statistical operations
data = np.array([10, 20, 30, 40, 50])

print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Standard Deviation:", np.std(data))
print("Variance:", np.var(data))
print("Maximum:", np.max(data))
print("Minimum:", np.min(data))