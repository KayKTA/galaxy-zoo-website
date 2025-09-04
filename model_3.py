import streamlit as st
from utils.ui import inject_css, two_col_layout
inject_css()

st.header("Classification en 7 Catégories")

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
    :blue-badge[Round Elliptical]
    :orange-badge[Cigar]
    :orange-badge[Edge-on Disk]
    :violet-badge[Spiral]
    :violet-badge[Barred Spiral]
    :gray-badge[No Bar Or Spiral]
    """
)
two_col_layout(
    model_name="predictCNN7",
    model_name2="predict6",
    model_label="Modèle CNN",
    model_label2="Modèle VGG16"
)
