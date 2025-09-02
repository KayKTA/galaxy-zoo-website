import requests
import streamlit as st
from .config import PREDICT_ENDPOINT

def predict_category(uploaded_file):
    files = {"file": uploaded_file.getvalue()}
    response = requests.post(PREDICT_ENDPOINT, files=files)
    response.raise_for_status()
    return response.json()
