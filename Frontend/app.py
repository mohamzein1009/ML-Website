import streamlit as st
import requests

st.title("ML Template Runner")

script_name = st.selectbox("Choose a script:", ["Data Exploration.ipynb", "Data Modelling.ipynb", "Data Preparation.ipynb"])
run_button = st.button("Run Script")

if run_button:
    response = requests.post("https://ml-website-1da5.onrender.com", json={"script": script_name})
    st.text(response.json())
