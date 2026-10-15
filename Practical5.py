import pandas as pd

# Create dataset
data = {
    'Name': ['Amit', 'Neha', 'Rahul', 'Priya', 'Sneha'],
    'Marks': [85, 92, 67, 95, 75],
    'Age': [20, 21, 19, 20, 22]
}

df = pd.DataFrame(data)

print("Original Dataset:\n", df)

# Filtering
print("\nStudents scoring above 80:")
print(df[df['Marks'] > 80])

# Sorting
print("\nStudents sorted by marks:")
print(df.sort_values(by='Marks', ascending=False))

# Conditional selection
print("\nStudents with marks >= 80 and age <= 21:")
print(df[(df['Marks'] >= 80) & (df['Age'] <= 21)])

# Select specific columns
print("\nSelected Columns:")
print(df[['Name', 'Marks']])