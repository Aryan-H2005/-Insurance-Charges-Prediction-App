import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("model.pkl")

st.title("🏥Insurance Charges Prediction App")

st.write("Enter the details below to predict insurance charges")

# User inputs
age = st.slider("Age", 18, 100, 30)
sex = st.selectbox("Sex", ["male","female"])
bmi = st.number_input("BMI", 10.0, 50.0, 25.0)
children = st.slider("Children",0,5,0)
smoker = st.selectbox("Smoker",["yes","no"])
region = st.selectbox("Region",["northeast","northwest","southeast","southwest"])

# Convert inputs to dataframe
input_data = pd.DataFrame({
    "age":[age],
    "bmi":[bmi],
    "children":[children],
    "sex_male":[1 if sex=="male" else 0],
    "smoker_yes":[1 if smoker=="yes" else 0],
    "region_northwest":[1 if region=="northwest" else 0],
    "region_southeast":[1 if region=="southeast" else 0],
    "region_southwest":[1 if region=="southwest" else 0]
})

# Prediction
if st.button("Predict Charges"):
    prediction = model.predict(input_data)
    st.success(f"Estimated Insurance Charges: ${prediction[0]:.2f}")