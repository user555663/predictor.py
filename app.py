import streamlit as st
from r6econ import r6econ

st.set_page_config(page_title="R6 Econ Predictor", layout="wide")

st.title("🧠 Rainbow Six Econ Predictor")
st.write("This tool helps predict or understand R6 marketplace patterns.")

st.markdown("### Input your numbers (comma separated):")
user_input = st.text_input("Example: 35,66,12,166,10,120,16,98,66,33")

if user_input:
    try:
        input_list = [int(x.strip()) for x in user_input.split(",")]
        prediction = r6econ(input_list)
        st.success(f"Predicted next number: {prediction}")
    except Exception as e:
        st.error(f"Error: {e}")
