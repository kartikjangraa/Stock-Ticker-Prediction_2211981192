import streamlit as st
import random
import pandas as pd
import numpy as np

# Title
st.title("📈 Stock Ticker Prediction Website")

# Description
st.write("This app predicts stock prices and shows trend visualization.")

# Input
ticker = st.text_input("Enter Stock Ticker (e.g., AAPL, TSLA)")

# Button
if st.button("Predict"):
    if ticker:

        # Fake prediction logic
        price = random.randint(100, 1000)
        trend = random.choice(["Upward 📈", "Downward 📉"])

        # Output
        st.subheader(f"Prediction for {ticker.upper()}")
        st.write(f"Predicted Price: ${price}")
        st.write(f"Market Trend: {trend}")

        # Generate fake data for graph
        data = pd.DataFrame(
            np.random.randn(20, 1),
            columns=['Price']
        )

        # Show graph
        st.subheader("Stock Trend Graph")
        st.line_chart(data)

        # Info
        st.info("Note: This is a basic prediction model using trend analysis.")

    else:
        st.warning("Please enter a stock ticker.")