import streamlit as st
import requests

FASTAPI_BASE_URL = "http://fastapi-container:8000"

st.title("Streamlit ↔ FastAPI Demo")

# 헬스체크 버튼
if st.button("Check FastAPI Health"):
    try:
        res = requests.get(f"{FASTAPI_BASE_URL}/health", timeout=3)
        st.write("Status:", res.json())
    except Exception as e:
        st.error(f"Error: {e}")
