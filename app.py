import streamlit as st
import numpy as np
import joblib

# load model
model = joblib.load("model.pkl")

st.title("Loan Prediction System")

st.write("Enter Applicant Details")

gender = st.selectbox("Gender", ["Male","Female"])
married = st.selectbox("Married", ["Yes","No"])
income = st.number_input("Applicant Income")
loan_amount = st.number_input("Loan Amount")
credit_history = st.selectbox("Credit History", [1,0])

# convert inputs
gender = 1 if gender=="Male" else 0
married = 1 if married=="Yes" else 0

input_data = np.array([[gender,married,income,loan_amount,credit_history]])

if st.button("Predict Loan Status"):

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("Loan Approved")
    else:
        st.error("Loan Rejected")