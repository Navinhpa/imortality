#Linear Regression (for Advanced Learners)
Consider a csv file data.csv which contains data on 'Number of hours studied' and 'ExamScore'. Using this csv file, we will build a simple finear regression model. Add the following code in main.py file on Github:
import streamlit as st
Import pandas as pd
from sklearn.model selection import train test split
from sklearn.linear model import LinearRegression
Load data from CSV (Ensure the file has "HouraStudied" and "ExamScore" columns)
df pd.read_csv("Data.csv")
Split data into Features (X) and Target (y)
Xdf [['HoursStudied']]
y df ['ExamScore']
st.dataframe (df)
