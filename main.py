Linear Regression (for Advanced Learners)
Consider a csv file data.csv which contains data on 'Number of hours studied' and 'ExamScore'. Using this csv file, we will build a simple finear regression model. Add the following code in main.py file on Github:
import streamlit as st
Import pandas as pd
from sklearn.model selection import train test split
from sklearn.linear model import LinearRegression
Load data from CSV (Ensure the file has "HouraStudied" and "ExamScore" columns)
df pd.read_csv("data.csv")
Split data into Features (X) and Target (y)
Xdf [['HoursStudied']]
y df ['ExamScore']
Train-Test Split (80% training, 20% testing)
X_train, X_test, y_train, y test -train_test_split(X, y, test_size-0.2, random
state-42)
Train the model
model LinearRegression ()
model.fit (X_train, y_train)
Streamlit User Interface
st.title(" Exam Score Predictor")
st.write("Enter hours studied to predict the exam score.")
User Input
hours st.number_input("Hours Studied:", min value-0.0, step-0.1)
Predict Button
if st.button ("Predict Score"):
predicted_score model.predict([[hours]]) [0]
st.success("☑ Predicted Score: (predicted_score:.2f}")
Show Sample Data
st.write("### Sample Training Data")
st.dataframe (df)
