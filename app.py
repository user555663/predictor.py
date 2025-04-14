import streamlit as st
from predictor import r6econ  # ✅ no Discord bot here

st.set_page_config(page_title="R6 Econ Predictor", layout="wide")

st.title("🔍 R6 Market Snipe Predictor")
st.markdown("Enter your price history to predict the next possible value:")

user_input = st.text_input("Comma-separated values", "35,66,12,166,10,120,16,98,66,33")

if user_input:
    try:
        data = [int(x.strip()) for x in user_input.split(",")]
        result = r6econ(data)
        st.success(f"Predicted next value: {result}")
    except Exception as e:
        st.error(f"Something went wrong: {e}")
