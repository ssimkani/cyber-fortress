# firebase_db.py
import os
import base64
import firebase_admin
from firebase_admin import credentials, firestore
import streamlit as st
from utils.config import FIREBASE_CRED

# Config
firebase_cred = FIREBASE_CRED

@st.cache_resource
def initialize_firebase():
    if not firebase_admin._apps:
        cred = credentials.Certificate(firebase_cred)
        return firebase_admin.initialize_app(cred)
    return firebase_admin.get_app()

# Initialize immediately when this file is imported
firebase_app = initialize_firebase()

db = firestore.client()

def save_user_data(uid: str, notes_txt: str):
        db.collection("users").document(uid).collection("notes").document("notes_txt").set(
            {"text": notes_txt,
             "timestamp": firestore.SERVER_TIMESTAMP
             })


def load_user_data(uid: str):
    doc = (
        db.collection("users")
        .document(uid)
        .collection("notes")
        .document("notes_txt")
        .get()
    )
    data = doc.to_dict()
    return data["text"] if doc.exists else ""
