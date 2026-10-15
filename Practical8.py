import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create dataset
data = {
    'Study_Hours': [1, 2, 3, 4, 5],
    'Marks': [30, 40, 55, 70, 90],
    'Attendance': [50, 60, 70, 80, 90]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

# Scatter plot
plt.scatter(df['Study_Hours'], df['Marks'])
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.show()

# Correlation heatmap
correlation = df.corr()

sns.heatmap(correlation, annot=True)
plt.title("Correlation Heatmap")
plt.show()