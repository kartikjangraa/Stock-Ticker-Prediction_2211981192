import streamlit as st
import random
import pandas as pd
import numpy as np

# Page config
st.set_page_config(page_title="Stock Predictor", page_icon="📈", layout="wide")

# Custom CSS (for better UI)
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
        color: white;
    }
    .stMetric {
        background-color: #1c1f26;
        padding: 10px;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("📈 Stock Ticker Prediction Dashboard")
st.markdown("### AI-based Stock Trend Analysis (Prototype)")

# Sidebar
st.sidebar.header("⚙️ Settings")
ticker = st.sidebar.text_input("Enter Stock Ticker", "AAPL")
days = st.sidebar.slider("Select Days of Prediction", 10, 100, 30)

# Button
if st.sidebar.button("Predict"):

    # Fake prediction
    price = random.randint(100, 1000)
    trend = random.choice(["Upward 📈", "Downward 📉"])

    # Layout (columns)
    col1, col2, col3 = st.columns(3)

    col1.metric("📌 Ticker", ticker.upper())
    col2.metric("💰 Predicted Price", f"${price}")
    col3.metric("📊 Trend", trend)

    st.markdown("---")

    # Generate smoother data
    data = pd.DataFrame(
        np.cumsum(np.random.randn(days, 1)),
        columns=['Price']
    )

    # Chart
    st.subheader("📉 Stock Price Trend")
    st.line_chart(data)

    # Extra insights
    st.markdown("### 📊 Insights")
    st.success("Market is showing stable movement." if "Upward" in trend else "Market shows possible decline.")

    # Progress bar (cool UI)
    st.markdown("### Confidence Level")
    st.progress(random.randint(50, 95))

else:
    st.info("👈 Enter details in sidebar and click Predict")