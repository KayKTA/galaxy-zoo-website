import streamlit as st
from backend.routes import predict_category
from utils.ui import inject_css, two_col_layout
inject_css()

st.header("🔭 Modèle CNN 7 Classes")


two_col_layout(
    model_name="predictCNN7"
)
