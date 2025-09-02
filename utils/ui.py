# utils/ui.py
from pathlib import Path
import streamlit as st

def inject_css(path: str = "static/styles.css"):

    css = Path(path).read_text()
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
