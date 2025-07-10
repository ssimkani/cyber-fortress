# src/config.py
import streamlit as st

# === Embedding Model ===
EMBEDDING_MODEL = "models/text-embedding-004"

# === Model ===
GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
MODEL_NAME = "gemini-1.5-flash"

# === FIREBASE Settings ===
FIREBASE_API_KEY = st.secrets["FIREBASE_API_KEY"]
FIREBASE_CRED = "utils/firebase_cred.json"

# === PINECONE Settings ===
PINECONE_API_KEY = st.secrets["PINECONE_API_KEY"]
PINECONE_INDEX_NAME = "cyber-fortress"

# === Chunking Settings ===
CHUNK_SIZE = 1500
CHUNK_OVERLAP = 150
NUM_CHUNKS = 4

# === Streamlit UI ===
APP_TITLE = "🛡️ Cyber Fortress"
