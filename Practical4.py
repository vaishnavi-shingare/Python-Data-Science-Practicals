import pandas as pd
import numpy as np

# Create dataset
data = {
    'Name': ['Amit', 'Neha', 'Rahul', 'Neha'],
    'Marks': [85, np.nan, 78, np.nan],
    'Age': [20, 21, 19, 21]
}

df = pd.DataFrame(data)

print("Original Dataset:\n", df)

# Handle missing values
df['Marks'] = df['Marks'].fillna(df['Marks'].mean())

# Remove duplicate rows
df = df.drop_duplicates()

# Modify dataset structure
df['Result'] = df['Marks'].apply(
    lambda x: 'Pass' if x >= 40 else 'Fail'
)

# Rename a column
df = df.rename(columns={'Marks': 'Score'})

print("\nPreprocessed Dataset:\n", df)