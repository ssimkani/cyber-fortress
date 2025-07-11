# pages/notes.py

import streamlit as st
from streamlit.runtime.caching import cache_data
from streamlit_ace import st_ace
import time
from utils.firebase_db import save_user_data
from utils.vector_store import upsert_chunks
from utils.split_text import split_text
from utils.config import APP_TITLE


# Block access if user is not logged in
if "uid" not in st.session_state:
    st.warning("Please log in to access your notes.")
    time.sleep(1)
    st.switch_page("login.py")
    st.stop()

st.set_page_config(page_title=APP_TITLE, layout="wide")

st.title("📝 Notes")
st.markdown(
    "<style>" + open("./style/style_notes.css").read() + "</style>", unsafe_allow_html=True
)

# === Code Editor with Line Numbers ===
if "notes" not in st.session_state:
    st.session_state["notes"] = ""

notes = st_ace(
    value=st.session_state["notes"],
    language="text",
    theme="monokai",
    keybinding="vscode",
    font_size=14,
    tab_size=4,
    show_gutter=True,
    wrap=True,
    auto_update=True,
    height=400,
    key="ace-editor",
)

uid = st.session_state["uid"]
if st.button("🔼 Save"):
    try:
        # Clear cache to ensure fresh data
        cache_data.clear() 
        
        # Save notes
        st.session_state["notes"] = notes
        save_user_data(uid, notes)

        # Save vector store
        chunks = split_text(notes)
        upsert_chunks(uid, chunks)

        st.success("Notes and vector store updated successfully.")

    except Exception as e:
        st.error(f"Failed to save: {e}")

    st.session_state["reset_chat"] = True
    time.sleep(1)
    st.rerun()
