
# 1. Library Import
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

# 2. Dataset Preparation
iris = load_iris()
X = iris.data
y = iris.target

# 3. Data Splitting
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4. Model Creation
model = DecisionTreeClassifier(random_state=42)

# 5. Model Training
model.fit(X_train, y_train)

# 6. Prediction
y_pred = model.predict(X_test)

# 7. Model Evaluation
accuracy = accuracy_score(y_test, y_pred)
print("Model Accuracy:", accuracy)

# 8. Classification Output
print("\nActual Classes:", y_test)
print("Predicted Classes:", y_pred)

print("\nClassification Report:")
print(classification_report(
    y_test, y_pred, target_names=iris.target_names
))

# Predict a new sample
sample = [[5.1, 3.5, 1.4, 0.2]]
prediction = model.predict(sample)
print("Predicted Flower:", iris.target_names[prediction[0]])
