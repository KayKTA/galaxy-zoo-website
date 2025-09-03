import streamlit as st
from backend.routes import predict_category
from utils.ui import inject_css
inject_css()


st.header("🔭 Modèle CNN 7 Classes")
# uploaded_file = st.file_uploader("Upload une image de galaxie", type=["png","jpg","jpeg"])
# if uploaded_file:
#     st.image(uploaded_file, use_container_width=False)

# if st.button("Predict"):
#     predict_category(uploaded_file)


uploaded = st.file_uploader("Upload une galaxie", type=["png","jpg","jpeg"])
if uploaded:
    st.image(uploaded, use_container_width=False)

    if st.button("Classifier"):
        with st.spinner("Analyse en cours..."):
            result = predict_category(uploaded, "predict6")
        # st.success(f"Résultat : {result['predicted_class']}")
        st.success(f"Résultat : {result['predicted_class']} ({result['probability']:.2%})")
