import numpy as np

# Create an array
data = np.array([10, 20, 30, 40, 50])

# Calculate statistical values
print("Data:", data)
print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Variance:", np.var(data))
print("Standard Deviation:", np.std(data))

# Calculate correlation
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

correlation = np.corrcoef(x, y)[0, 1]
print("Correlation:", correlation)