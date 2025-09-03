import streamlit as st
from utils.ui import inject_css
inject_css()

st.set_page_config(page_title="Galaxy Classifier", page_icon="🌌", layout="wide")

pages = {
    "": [
        st.Page("home.py", title="Accueil", icon="🏠"),
    ],
    "🪐 Modèles": [
        st.Page("model_1.py", title="Model CNN 3", icon="🌞"),
        st.Page("model_2.py", title="Model CNN 7", icon="🚀"),
        st.Page("model_3.py", title="Model VGG16 3", icon="🌌"),
        st.Page("model_4.py", title="Model VGG16 7", icon="☄️"),
    ],
}

pg = st.navigation(pages)
pg.run()
