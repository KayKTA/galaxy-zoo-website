import streamlit as st
import streamlit as st
import datetime
import numpy as np
import pandas as pd
import requests
import math

URL = 'https://galaxyzoo-358196745530.europe-west1.run.app'
model = 'bucket-galaxy-zoo/models/20250901-0739203_CAT_MODEL_SMALL_NICOLAS_256-256X1000_EPOCHS_30.h5'

def say_hello():

    response = requests.get(f"{URL}/")
    if response.ok :
        return True, response.json()
    else :
        return False, f"{response.status_code}: {response.json()} "

def predict_category():
    files = {"file": uploaded_file.getvalue()}
    response = requests.post(f"{URL}/predict", files=files)

    if response.status_code == 200:
        st.json(response.json())
    else:
        st.error(f"Error: {response.status_code}")

st.title("Galaxy Zoo")

uploaded_file = st.file_uploader("Upload galaxy image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Prévisualiser l’image
    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

    # Bouton pour envoyer au backend
    if st.button("Predict"):
        predict_category()
