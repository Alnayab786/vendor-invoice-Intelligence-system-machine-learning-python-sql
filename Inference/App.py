import streamlit as st
import pandas as pd
from Predict_freight import predict_freight_cost

# ----------------------------------------------------------
# Page Configuration
# ----------------------------------------------------------
st.set_page_config(
    page_title="Vendor Invoice Intelligence Portal",
    page_icon="📦",
    layout="wide"
)

# ----------------------------------------------------------
# Header Section
# ----------------------------------------------------------
st.markdown("""
# 📦 Vendor Invoice Intelligence Portal
### AI-Driven Freight Cost Prediction

This internal analytics portal leverages machine learning to:

- **Forecast freight costs accurately**
- **Reduce financial leakage and manual workload**
""")

st.divider()

# ----------------------------------------------------------
# Sidebar
# ----------------------------------------------------------
selected_model = st.sidebar.selectbox(
    "🔍 Select Model",
    ["Freight Cost Prediction"]
)

st.sidebar.markdown("""
---
### Business Impact

- 📈 Improved Cost Forecasting
- 🛡️ Reduce Invoice Fraud & Anomalies
- ⚡ Faster Finance Operations
""")

# ----------------------------------------------------------
# Freight Cost Prediction
# ----------------------------------------------------------
if selected_model == "Freight Cost Prediction":

    st.subheader("🚚 Freight Cost Prediction")

    st.markdown("""
    **Objective:**

    Predict freight cost for a vendor using **Quantity** and **Invoice Dollars**
    to support budgeting, forecasting, and vendor negotiations.
    """)

    with st.form("freight_form"):

        col1, col2 = st.columns(2)

        with col1:
            quantity = st.number_input(
                "📦 Quantity",
                min_value=1,
                value=1200
            )

        with col2:
            dollars = st.number_input(
                "💰 Invoice Dollars",
                min_value=1.0,
                value=18500.0
            )

        submit_freight = st.form_submit_button(
            "🧮 Predict Freight Cost"
        )

    if submit_freight:

        input_data = pd.DataFrame({
            "Quantity": [quantity],
            "Dollars": [dollars]
        })

        prediction = predict_freight_cost(input_data)

        st.success("Prediction completed successfully.")

        # If prediction is a DataFrame
        if isinstance(prediction, pd.DataFrame):
            freight_cost = prediction["Predicted_Freight"].iloc[0]
        else:
            # If prediction is a NumPy array/list
            freight_cost = prediction[0]

        st.metric(
            label="📊 Estimated Freight Cost",
            value=f"${freight_cost:,.2f}"
        )