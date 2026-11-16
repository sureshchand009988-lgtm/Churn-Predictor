
import streamlit as st

st.set_page_config(
    page_title="About | Customer Churn Predictor",
    layout="wide"
)

st.title("About Our Project")

st.markdown("""
# Customer Churn Prediction

## Project Overview

Customer Churn Prediction is a machine learning application
designed to identify customers who are likely to discontinue
a company's services.

The project uses customer information to identify patterns
associated with churn. A Random Forest Classifier is used
to make predictions, supported by data preprocessing and
SMOTE to handle class imbalance.

## Project Objectives

- Analyze customer data to understand churn patterns.
- Develop a machine learning model for customer churn prediction.
- Handle imbalanced data using SMOTE.
- Apply suitable preprocessing techniques to different features.
- Help businesses make informed customer retention decisions.

---

## Technologies Used

- **Python:** Main programming language used for development.
- **Streamlit:** Used to build the interactive web application.
- **Pandas:** Used for data manipulation and analysis.
- **NumPy:** Used for numerical computations.
- **Scikit-learn:** Used for preprocessing and Random Forest implementation.
- **Imbalanced-learn:** Used for SMOTE and pipeline implementation.
- **Matplotlib and Seaborn:** Used for data visualization.

---

## Working Methodology

**1. Data Collection**

Loading and exploring the customer dataset to understand
its structure and features.

**2. Data Preprocessing**

Using ColumnTransformer to apply appropriate preprocessing
to different numerical and categorical columns.

**3. Handling Class Imbalance**

Applying SMOTE to the training data to address the imbalance
between churn and non-churn classes.

**4. Model Training**

Training a Random Forest Classifier using an integrated
machine learning pipeline.

**5. Customer Prediction**

Using the trained pipeline to predict whether a customer
is likely to leave the company's services.

---

## Key Features

- Random Forest-based customer churn prediction.
- Automated preprocessing using ColumnTransformer.
- SMOTE for handling imbalanced training data.
- Integrated machine learning pipeline.
- Interactive Streamlit dashboard.

---

## Project Goal

The primary goal of this project is to use machine learning
to identify customers who may discontinue a company's services.

These predictions can help businesses understand customer
behaviour and develop better customer retention strategies.

---

## Developed By

**Yash**

B.Tech - Information Technology
""")
