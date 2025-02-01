import streamlit as st
import requests

st.title("ML Template Runner")

script_name = st.selectbox("Choose a script:", ["data_cleaning.py", "model_training.py", "visualization.py"])
run_button = st.button("Run Script")

if run_button:
    response = requests.post("http://127.0.0.1:5000/run_template", json={"script": script_name})
    st.text(response.json())
