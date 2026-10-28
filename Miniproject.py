import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Dataset preparation (sample data for practical demonstration)
data = {
    "Study_Hours": [1,2,3,4,5,6,7,2,4,6,8,3,5,7,1,4,6,8,2,5,7,3,6,9,4,5,8,2,7,9],
    "Attendance": [55,60,65,70,75,80,90,58,72,85,95,68,78,88,50,74,82,96,62,76,91,66,84,98,71,79,93,57,89,97],
    "Previous_Score": [35,42,48,55,60,68,82,40,57,72,88,50,63,79,30,58,70,92,44,65,85,49,74,95,56,67,90,38,81,96],
    "Assignments_Completed": [2,3,4,5,6,7,9,3,5,8,10,4,6,9,1,5,7,10,3,6,9,4,8,10,5,6,10,2,9,10]
}
df = pd.DataFrame(data)

# Create categorical outcome for this demonstration dataset
score = (0.35 * df["Study_Hours"] + 0.025 * df["Attendance"]
         + 0.025 * df["Previous_Score"] + 0.45 * df["Assignments_Completed"])
df["Result"] = np.where(score >= 5.2, "Pass", "Fail")

# Add missing values to demonstrate data preprocessing
df.loc[4, "Attendance"] = np.nan
df.loc[17, "Previous_Score"] = np.nan
# NumPy array and matrix operations
arr = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
print("NumPy Array:\n", arr)
print("Array sum:", np.sum(arr))
print("Array mean:", np.mean(arr))
print("Matrix transpose:\n", arr.T)
print("Matrix multiplication (arr @ arr.T):\n", np.dot(arr, arr.T))

# Pandas data inspection
print("\nFirst five rows:\n", df.head())
print("\nDataset shape:", df.shape)
print("\nData types:\n", df.dtypes)
print("\nStatistical summary:\n", df.describe())
print("\nMissing values before preprocessing:\n", df.isnull().sum())

# Data preprocessing: replace missing values with column medians
df["Attendance"] = df["Attendance"].fillna(df["Attendance"].median())
df["Previous_Score"] = df["Previous_Score"].fillna(df["Previous_Score"].median())
print("\nMissing values after preprocessing:\n", df.isnull().sum())

# Visualization
df["Result"].value_counts().reindex(["Fail", "Pass"]).plot(kind="bar")
plt.title("Student Result Distribution")
plt.xlabel("Result")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.show()

plt.scatter(df["Study_Hours"], df["Previous_Score"])
plt.title("Study Hours vs Previous Score")
plt.xlabel("Study Hours")
plt.ylabel("Previous Score")
plt.tight_layout()
plt.show()

# Prepare data and split into training and testing sets
features = ["Study_Hours", "Attendance", "Previous_Score", "Assignments_Completed"]
X = df[features]
y = df["Result"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)

# Scale features and train logistic regression classifier
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
model = LogisticRegression(random_state=42)
model.fit(X_train, y_train)

# Prediction and evaluation
y_pred = model.predict(X_test)
print("\nActual results:", list(y_test))
print("Predicted results:", list(y_pred))
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification report:\n", classification_report(y_test, y_pred))

# Predict result for a new student
new_student = pd.DataFrame([[5, 80, 65, 7]], columns=features)
new_student_scaled = scaler.transform(new_student)
print("New student prediction:", model.predict(new_student_scaled)[0])

