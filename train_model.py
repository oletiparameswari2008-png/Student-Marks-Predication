import pandas as pd

# Load the dataset
data = pd.read_csv("data/student_marks.csv")

# Input features
X = data[[
    "Hours_Studied",
    "Previous_Score",
    "Attendance",
    "Assignments_Completed"
]]

# Target value
y = data["Final_Marks"]

print("Input Features:")
print(X.head())

print("\nTarget Values:")
print(y.head())

from sklearn.model_selection import train_test_split

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\nTraining data size:", len(X_train))
print("Testing data size:", len(X_test))

from sklearn.linear_model import LinearRegression

# Create the model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

print("\nModel training completed successfully!")

# Make predictions on the test data
y_pred = model.predict(X_test)

print("\nActual Marks:")
print(y_test.values)

print("\nPredicted Marks:")
print(y_pred)

from sklearn.metrics import r2_score, mean_absolute_error

# Calculate model performance
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

print("\nModel Evaluation:")
print("R2 Score:", r2)
print("Mean Absolute Error:", mae)

import joblib

# Save the trained model
joblib.dump(model, "models/student_marks_model.pkl")

print("\nModel saved successfully!")