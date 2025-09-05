from pathlib import Path
import streamlit as st
from backend.routes import predict_category

def inject_css(path: str = "static/styles.css"):

    css = Path(path).read_text()
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

def show_result(model_label, pred_class, proba, bckg = '#7C3AED22'):
    st.markdown(f"""
    <div style="
        background: {bckg};
        padding: 1.5rem;
        border-radius: 16px;
        text-align: center;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        font-family: 'Inter', sans-serif;">
        <h2 style="color:#7C3AED; margin:0; font-size:1.8rem;">
            {model_label}:
        </h2>
        <p style="font-size:1.4rem; margin-top:.5rem;">
            <b>{pred_class}</b> <hr>
            <b style="font-size:1.5rem; color:green;">
                Confiance : {proba:.2%}
            </b>
        </p>
    </div>
    """, unsafe_allow_html=True)

def two_col_layout( model_name: str, model_name2: str, model_label: str, model_label2: str):
    col_left, col_right = st.columns([3, 2])

    with col_left:
        uploaded = st.file_uploader("📤 Upload une galaxie", type=["png","jpg","jpeg"])
        if uploaded and st.button("Classifier", use_container_width=True, type="primary"):
            with st.spinner("Analyse en cours..."):
                result = predict_category(uploaded, model_name)
                result2 = predict_category(uploaded, model_name2)

            sub_col_left, sub_col_right = st.columns([2, 2])
            with sub_col_left:
                show_result(
                    model_label,
                    result["predicted_class"],
                    result["probability"],
                )
            with sub_col_right:
                show_result(
                    model_label2,
                    result2["predicted_class"],
                    result2["probability"],
                    bckg='#2D97EB45'
                )

    with col_right:
        if uploaded:
            st.image(uploaded, caption="Image uploadée", use_container_width=True)
