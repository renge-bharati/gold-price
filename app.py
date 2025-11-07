# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Title and Description
# -----------------------------
st.title("📈 Gold Price Data Dashboard")
st.markdown("""
This app visualizes historical **Gold Price Data**.
Upload your dataset or use the default sample to explore trends and insights.
""")

# -----------------------------
# File Upload Section
# -----------------------------
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("✅ File uploaded successfully!")
else:
    st.info("Using default sample dataset (gold_price_data.csv)")
    df = pd.read_csv("gold_price_data.csv")

# -----------------------------
# Display Dataset
# -----------------------------
st.subheader("📊 Data Preview")
st.dataframe(df.head())

# -----------------------------
# Data Summary
# -----------------------------
st.subheader("📋 Dataset Summary")
st.write(df.describe())

# -----------------------------
# Plotting Section
# -----------------------------
st.subheader("📆 Gold Price Trends")

# Ensure Date column is datetime
if "Date" in df.columns:
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.sort_values("Date")

    # Line chart for Close Price
    st.line_chart(df.set_index("Date")["Close"], use_container_width=True)

    # Optional: Multiple prices
    st.line_chart(df.set_index("Date")[["Open", "High", "Low", "Close"]])
else:
    st.error("❌ 'Date' column not found. Please check your CSV file structure.")

# -----------------------------
# Footer
# -----------------------------
st.markdown("""
---
📁 **Note:** Replace `gold_price_data.csv` with your actual dataset in the same folder.  
Developed with ❤️ using [Streamlit](https://streamlit.io)
""")
