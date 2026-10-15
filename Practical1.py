import numpy as np

# Create an array
arr = np.array([10, 20, 30, 40, 50, 60])

print("Original Array:", arr)

# Indexing
print("Element at index 2:", arr[2])

# Slicing
print("Sliced Array:", arr[1:4])

# Reshaping
matrix = arr.reshape(2, 3)
print("Reshaped Array:\n", matrix)

# Vectorized operations
print("Addition:", arr + 5)
print("Multiplication:", arr * 2)
print("Square:", arr ** 2)