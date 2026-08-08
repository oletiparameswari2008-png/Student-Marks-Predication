# 🎓 Student Marks Prediction

## 1. Project Overview

Student Marks Prediction is a Machine Learning project that predicts a student's final marks based on their academic details.

The project uses **Linear Regression** to predict the final marks of a student based on:

- Hours Studied
- Previous Score
- Attendance
- Assignments Completed

A **Streamlit web application** is also created so users can enter student details and get predicted final marks.


## 2. Objectives

The main objectives of this project are:

- To predict students' final marks using Machine Learning.
- To understand and analyze student academic data.
- To train a Linear Regression model.
- To evaluate the performance of the trained model.
- To create an interactive web application using Streamlit.


## 3. Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Streamlit
- VS Code
- Git
- GitHub


## 4. Dataset

The dataset contains **30 student records**.

### Input Features

| Feature | Description |
|---|---|
| Hours_Studied | Number of hours studied by the student |
| Previous_Score | Student's previous examination score |
| Attendance | Student's attendance percentage |
| Assignments_Completed | Number of assignments completed |

### Target Variable

**Final_Marks** – The final marks obtained by the student.


## 5. Data Analysis

The dataset was loaded using Pandas and analyzed to understand:

- Number of records
- Data types
- Dataset statistics
- Minimum and maximum values
- Average values
- Input features
- Target values

The dataset contains **30 rows and 5 columns**.


## 6. Input Features and Target

The input features are:

```text
Hours_Studied
Previous_Score
Attendance
Assignments_Completed


## 📂 Project Structure

Student-Marks-Predication/
│
├── data/
│   └── student_marks.csv
│
├── models/
│   └── student_marks_model.pkl
│
├── venv/
│
├── .gitignore
├── app.py
├── README.md
└── train_model.py

AUTHOR
O. Naga Parameswari