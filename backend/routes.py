import requests
import streamlit as st

def predict_category(uploaded_file, model_name):
    try:
        # API_URL = st.secrets["API_URL"]
        API_URL = "https://galaxyzoo-358196745530.europe-west1.run.app"
        full_url = f"{API_URL}/{model_name}"

        content = uploaded_file.getvalue()
        filename = getattr(uploaded_file, "name", "upload.bin")
        mime = getattr(uploaded_file, "type", None) or "application/octet-stream"

        files = {"file": (filename, content, mime)}

        # Headers spécifiques pour Cloud Run
        headers = {
            'User-Agent': 'Mozilla/5.0 (compatible; StreamlitApp/1.0)',
            'Accept': 'application/json',
        }

        st.write(f"🔍 URL appelée: {full_url}")

        res = requests.post(
            full_url,
            files=files,
            headers=headers,
            timeout=60,  # Cloud Run peut être lent
            allow_redirects=True
        )

        st.write(f"✅ Status: {res.status_code}")
        st.write(f"✅ Response headers: {dict(res.headers)}")

        res.raise_for_status()
        return res.json()

    except requests.exceptions.ConnectionError as e:
        st.error(f"❌ Erreur de connexion vers {full_url}")
        st.error(f"Votre API répond bien à la racine, vérifiez l'endpoint /{model_name}")
        raise
    except Exception as e:
        st.error(f"❌ Erreur: {str(e)}")
        raise
