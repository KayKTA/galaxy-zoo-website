import requests
import streamlit as st
from .config import API_URL

def predict_category(uploaded_file, model_name):
    print(f"in predict {model_name}")

    content = uploaded_file.getvalue()
    if not content:
        raise ValueError("Fichier vide")

    filename = getattr(uploaded_file, "name", "upload.bin")
    mime = getattr(uploaded_file, "type", None) or "application/octet-stream"

    files = {
        "file": (filename, content, mime)
    }

    res = requests.post(f"{API_URL}/{model_name}", files=files)
    print(res.status_code, res.headers.get("content-type")); print(res.text)
    res.raise_for_status()
    return res.json()
