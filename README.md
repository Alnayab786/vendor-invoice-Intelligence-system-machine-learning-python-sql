# 🚚 Vendor Invoice Intelligence Portal

## Overview

Vendor Invoice Intelligence Portal is a Machine Learning-powered application that predicts freight costs from vendor invoice data. The solution helps finance and procurement teams improve forecasting accuracy, reduce manual effort, and support data-driven decision-making.

## Features

* 📦 Freight Cost Prediction
* 📊 Interactive Streamlit Dashboard
* 🤖 Machine Learning-Based Forecasting
* 📈 Improved Cost Forecasting
* 🛡️ Reduced Invoice Fraud & Anomalies
* ⚡ Faster Finance Operations
* 💰 Better Budget Planning

---

## Project Structure

```text
Freight Cost/
│
├── App.py
├── train.py
├── Predict_freight.py
├── Data_processing.py
├── model_evaluation.py
│
├── Model/
│   └── predict_freight_model.pkl
│
└── inventory.db
```

---

## Technologies Used

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* Scikit-Learn
* Joblib
* Streamlit

### Database

* SQLite

---

## Machine Learning Workflow

### 1. Data Loading

Vendor invoice data is loaded from an SQLite database.

### 2. Data Preparation

Input Features:

* Quantity
* Dollars

Target Variable:

* Freight

### 3. Model Training

The following algorithms are trained and evaluated:

* Linear Regression
* Decision Tree Regression
* Random Forest Regression

### 4. Model Evaluation

Models are evaluated using:

* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)
* R² Score

### 5. Best Model Selection

The best-performing model is automatically selected and saved as:

```text
Model/predict_freight_model.pkl
```

---

## Installation

Install the required libraries:

```bash
pip install pandas numpy scikit-learn streamlit joblib
```

---

## Training the Model

Run:

```bash
python train.py
```

This will:

* Load invoice data
* Train multiple machine learning models
* Compare performance metrics
* Save the best model

---

## Running the Streamlit Application

Run:

```bash
streamlit run App.py
```

After execution, Streamlit will provide a local URL such as:

```text
http://localhost:8501
```

Open the URL in your browser.

---

## Dashboard Inputs

Users can enter:

* Quantity
* Invoice Dollars

Example:

```text
Quantity = 1200
Invoice Dollars = 18500
```

---

## Dashboard Output

The application predicts:

```text
Estimated Freight Cost
```

Example:

```text
Estimated Freight Cost: $98
```

---

## Business Benefits

### 📈 Improved Cost Forecasting

Provides accurate freight cost estimates for budgeting and planning.

### 🛡️ Reduced Invoice Fraud & Anomalies

Helps identify unusual freight costs and invoice discrepancies.

### ⚡ Faster Finance Operations

Reduces manual calculations and accelerates invoice review processes.

---

## Future Enhancements

* Vendor Risk Scoring
* Invoice Anomaly Detection
* Cost Optimization Recommendations
* Advanced Analytics Dashboard
* Batch Invoice Prediction
* Power BI Integration

---

## Author

**Al Nayab**
**Data Analyst**
**Email: nayabmansoori@gmail.com


Skills:

* Python
* SQL
* Data Analysis
* Machine Learning
* Streamlit
* Power BI
* SQLite
* Business Analytics
