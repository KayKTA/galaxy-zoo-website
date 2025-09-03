from pathlib import Path
import streamlit as st
from backend.routes import predict_category

def inject_css(path: str = "static/styles.css"):

    css = Path(path).read_text()
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

def show_result(pred_class, proba):
    st.markdown(f"""
    <div style="
        background: #7C3AED22;
        padding: 1.5rem;
        border-radius: 16px;
        text-align: center;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        font-family: 'Inter', sans-serif;">
        <h2 style="color:#7C3AED; margin:0; font-size:1.8rem;">
            🔭 Résultat
        </h2>
        <p style="font-size:1.3rem; margin-top:.5rem;">
            <b>{pred_class}</b> <br>
            <span style="font-size:1.1rem; color:#10B981;">
                Confiance : {proba:.2%}
            </span>
        </p>
    </div>
    """, unsafe_allow_html=True)

def two_col_layout( model_name: str):
    col_left, col_right = st.columns([3, 2])

    with col_left:
        uploaded = st.file_uploader("📤 Upload une galaxie", type=["png","jpg","jpeg"])
        if uploaded and st.button("Classifier", use_container_width=True, type="primary"):
            with st.spinner("Analyse en cours..."):
                result = predict_category(uploaded, model_name)
            show_result(
                result["predicted_class"],
                result["probability"],
            )

    with col_right:
        if uploaded:
            st.image(uploaded, caption="Image uploadée", use_container_width=True)
