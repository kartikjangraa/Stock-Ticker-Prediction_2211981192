import streamlit as st
import random
import pandas as pd
import numpy as np
import requests

# ---------------- NEWS FUNCTION ----------------
def get_news(company):
    api_key = st.secrets["NEWS_API_KEY"]  # 🔐 Secure
    url = f"https://newsdata.io/api/1/news?apikey={api_key}&q={company}&language=en"

    try:
        response = requests.get(url)
        data = response.json()

        articles = []
        if "results" in data:
            for article in data["results"][:10]:
                articles.append({
                    "title": article.get("title"),
                    "url": article.get("link"),
                    "source": article.get("source_id")
                })
        return articles
    except:
        return []

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Stock Predictor", page_icon="📈", layout="wide")

# ---------------- CUSTOM CSS ----------------
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

# ---------------- TITLE ----------------
st.title("📈 Stock Ticker Prediction Dashboard")
st.markdown("### AI-based Stock Trend Analysis (Prototype)")

# ---------------- SIDEBAR ----------------
st.sidebar.header("⚙️ Settings")
ticker = st.sidebar.text_input("Enter Stock Ticker", "AAPL")
days = st.sidebar.slider("Select Days of Prediction", 10, 100, 30)

# ---------------- BUTTON ----------------
if st.sidebar.button("Predict"):

    price = random.randint(100, 1000)
    trend = random.choice(["Upward 📈", "Downward 📉"])

    col1, col2, col3 = st.columns(3)
    col1.metric("📌 Ticker", ticker.upper())
    col2.metric("💰 Predicted Price", f"${price}")
    col3.metric("📊 Trend", trend)

    st.markdown("---")

    data = pd.DataFrame(
        np.cumsum(np.random.randn(days, 1)),
        columns=['Price']
    )

    st.subheader("📉 Stock Price Trend")
    st.line_chart(data)

    st.markdown("### 📊 Insights")
    st.success("Market is showing stable movement." if "Upward" in trend else "Market shows possible decline.")

    st.markdown("### Confidence Level")
    st.progress(random.randint(50, 95))

    # ---------------- NEWS ----------------
    st.markdown("---")
    st.subheader("📰 Top 10 Latest News")

    ticker_map = {
        "AAPL": "Apple",
        "TSLA": "Tesla",
        "GOOGL": "Google",
        "MSFT": "Microsoft",
        "AMZN": "Amazon"
    }

    company_name = ticker_map.get(ticker.upper(), ticker)

    news = get_news(company_name)

    if news:
        for i, article in enumerate(news, 1):
            st.markdown(f"**{i}. {article['title']}**")
            st.markdown(f"Source: {article['source']}")
            st.markdown(f"[Read more]({article['url']})")
            st.markdown("---")
    else:
        st.warning("No news found or API limit reached.")

else:
    st.info("👈 Enter details in sidebar and click Predict")