# Insurance Charges Prediction

## Project Overview

This project predicts **medical insurance charges** based on personal and health-related information using **Machine Learning**. The model is trained using the **Linear Regression algorithm** and deployed with **Streamlit** to provide an interactive web application.

The goal of the project is to demonstrate the complete **Data Science workflow**, including data preprocessing, model training, evaluation, and deployment.

---

## Problem Statement

Health insurance companies need to estimate **medical charges for individuals** based on their characteristics such as age, BMI, smoking status, and region.

This project builds a predictive model that estimates **insurance charges** for a person using machine learning.

---

## Dataset

The dataset used in this project contains the following features:

* **age** – Age of the person
* **sex** – Gender (male/female)
* **bmi** – Body Mass Index
* **children** – Number of children covered by insurance
* **smoker** – Whether the person smokes or not
* **region** – Residential area in the US
* **charges** – Medical insurance cost (target variable)

---

## Technologies Used

* Python
* Pandas
* Scikit-learn
* Streamlit
* Joblib

---

## Machine Learning Model

The project uses **Linear Regression** to predict insurance charges.

Steps involved:

1. Data loading and preprocessing
2. Converting categorical variables using one-hot encoding
3. Splitting data into training and testing sets
4. Training a Linear Regression model
5. Evaluating model performance using metrics

Evaluation Metrics:

* Mean Squared Error (MSE)
* Mean Absolute Error (MAE)

---

## Project Structure

```
Insurance-Charges-Prediction
│
├── insurance.csv
├── train_model.py
├── app.py
├── model.pkl
├── requirements.txt
└── README.md
```

---

## How to Run the Project

### 1 Install Dependencies

```
pip install -r requirements.txt
```

### 2 Train the Model

```
python train_model.py
```

### 3 Run the Streamlit App

```
streamlit run app.py
```

---

## Streamlit Application

The Streamlit web app allows users to input information such as:

* Age
* Sex
* BMI
* Number of children
* Smoking status
* Region

Based on these inputs, the model predicts the **estimated medical insurance charges**.

---

## Example Use Case

A user enters their personal information in the web interface. The model processes the inputs and predicts the expected insurance cost.

This type of model can help insurance companies estimate risk and pricing.

---

## Future Improvements

* Use advanced models like Random Forest or XGBoost
* Improve feature engineering
* Perform hyperparameter tuning
* Deploy the app on Streamlit Cloud

---
## Live Demo : https://insurance-charges-predict.streamlit.app/

## Author

Aryan Harke

Third Year Computer Science Student
