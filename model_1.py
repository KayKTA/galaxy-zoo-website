import streamlit as st
from backend.routes import predict_category
from utils.ui import inject_css
inject_css()

st.header("🔭 Modèle 50 Neurones")
img = st.file_uploader("Upload une image de galaxie", type=["png","jpg","jpeg"])
if img:
    st.image(img, use_container_width=True)
