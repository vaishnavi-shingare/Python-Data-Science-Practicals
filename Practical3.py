import pandas as pd

# Create a sample dataset
data = {
    'Name': ['Amit', 'Neha', 'Rahul', 'Priya'],
    'Marks': [85, 90, 78, 95],
    'Age': [20, 21, 19, 20]
}

df = pd.DataFrame(data)

# Display dataset
print("Dataset:\n", df)

# Initial inspection
print("\nFirst 5 Rows:\n", df.head())
print("\nDataset Information:")
df.info()

print("\nDescriptive Statistics:\n", df.describe())
print("\nColumn Names:", df.columns)
print("\nDataset Shape:", df.shape)