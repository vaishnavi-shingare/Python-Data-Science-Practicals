from sklearn.linear_model import LinearRegression

# Input: Study hours
X = [[1], [2], [3], [4], [5]]

# Output: Marks
y = [20, 30, 40, 50, 60]

# Create the model
model = LinearRegression()

# Train the model
model.fit(X, y)

# Predict marks for 6 hours of study
prediction = model.predict([[6]])

print("Study Hours: 6")
print("Predicted Marks:", prediction[0])

# Display model values
print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)