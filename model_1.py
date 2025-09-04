import streamlit as st
from backend.routes import predict_category
from utils.ui import inject_css, two_col_layout
inject_css()

st.header("Classification en 3 Catégories")
st.markdown("""
<style>
[data-testid="stBadge"] {
    font-size: 1.3rem !important;   /* texte plus grand */
    padding: 0.4rem 0.8rem !important; /* plus d’espace */
}
</style>
""", unsafe_allow_html=True)
st.markdown(
    """
    :blue-badge[Elliptical]
    :orange-badge[Edge-on/Cigar]
    :violet-badge[Spiral]
    """
)
two_col_layout(
    model_name="predictCNN",
    model_name2="predictVGG",
    model_label="Modèle CNN",
    model_label2="Modèle VGG16"
)
