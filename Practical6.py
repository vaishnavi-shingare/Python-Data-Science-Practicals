import pandas as pd

# Create a dataset
data = {
    'Department': ['Computer', 'IT', 'Computer', 'IT'],
    'Marks': [80, 90, 70, 85]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# Group by department and calculate average
print("\nAverage Marks:")
print(df.groupby('Department')['Marks'].mean())

# Calculate total marks
print("\nTotal Marks:")
print(df.groupby('Department')['Marks'].sum())

# Calculate maximum marks
print("\nMaximum Marks:")
print(df.groupby('Department')['Marks'].max())