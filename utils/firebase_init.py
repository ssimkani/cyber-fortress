import firebase_admin
from firebase_admin import credentials
import streamlit as st
import tempfile

def init_firebase():
    if not firebase_admin._apps:
        # Write the Firebase JSON string from secrets to a temp file
        with tempfile.NamedTemporaryFile(mode="w+", suffix=".json", delete=False) as f:
            f.write(st.secrets["firebase"]["json"])
            f.flush()
            cred = credentials.Certificate(f.name)
            firebase_admin.initialize_app(cred)