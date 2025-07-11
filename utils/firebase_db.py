# firebase_db.py
from firebase_admin import firestore
import streamlit as st
from utils.firebase_init import init_firebase

def get_db():
    init_firebase()
    return firestore.client()

def save_user_data(uid: str, notes_txt: str):
        db = get_db()
        db.collection("users").document(uid).collection("notes").document("notes_txt").set(
            {"text": notes_txt,
                "timestamp": firestore.SERVER_TIMESTAMP
                })


def load_user_data(uid: str):
    db = get_db()
    doc = (
        db.collection("users")
        .document(uid)
        .collection("notes")
        .document("notes_txt")
        .get()
    )
    data = doc.to_dict()
    return data["text"] if doc.exists else ""
