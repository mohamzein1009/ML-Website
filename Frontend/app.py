import streamlit as st
import requests

st.title("ML Template Runner")

script_name = st.selectbox("Choose a script:", ["data_cleaning.py", "model_training.py", "visualization.py"])
run_button = st.button("Run Script")

if run_button:
    response = requests.post("https://ml-website-1da5.onrender.com", json={"script": script_name})
    st.text(response.json())
