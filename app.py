import streamlit as st
import joblib
import pandas as pd

# Load the trained model
model = joblib.load("models/student_marks_model.pkl")

# Page title
st.title("🎓 Student Marks Prediction")

st.write("Enter the student's details to predict the final marks.")

# Input fields
hours_studied = st.number_input(
    "Hours Studied",
    min_value=0.0,
    max_value=24.0,
    value=5.0
)

previous_score = st.number_input(
    "Previous Score",
    min_value=0.0,
    max_value=100.0,
    value=60.0
)

attendance = st.number_input(
    "Attendance (%)",
    min_value=0.0,
    max_value=100.0,
    value=80.0
)

assignments_completed = st.number_input(
    "Assignments Completed",
    min_value=0,
    max_value=10,
    value=7
)

# Prediction button
if st.button("Predict Marks"):

    # Create input data
    input_data = pd.DataFrame({
        "Hours_Studied": [hours_studied],
        "Previous_Score": [previous_score],
        "Attendance": [attendance],
        "Assignments_Completed": [assignments_completed]
    })

    # Make prediction
    prediction = model.predict(input_data)

    # Display result
    st.success(f"Predicted Final Marks: {prediction[0]:.2f}")