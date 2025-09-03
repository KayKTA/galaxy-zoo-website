import streamlit as st
from backend.routes import predict_category
from utils.ui import inject_css
inject_css()

st.header("🔭 Modèle VGG16 3 Classes")

uploaded = st.file_uploader("Upload une galaxie", type=["png","jpg","jpeg"])
if uploaded:
    st.image(uploaded, use_container_width=False)

    if st.button("Classifier"):
        with st.spinner("Analyse en cours..."):
            result = predict_category(uploaded, "predictVGG")
        # st.success(f"Résultat : {result['predicted_class']}")
        st.success(f"Résultat : {result['predicted_class']} ({result['probability']:.2%})")
