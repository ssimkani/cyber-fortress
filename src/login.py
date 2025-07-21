import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import os
import time
from utils.firebase_auth import *
from utils.firebase_db import *
from utils.config import *


st.set_page_config(page_title=APP_TITLE, layout="wide")

# Redirect to chat page if user is already logged in
if "email" in st.session_state and "uid" in st.session_state:
    st.info("You are already logged in. Redirecting to chat page...")
    time.sleep(1)
    st.switch_page("pages/chat.py")

st.title(APP_TITLE)

mode = st.radio("Choose mode", ["Login", "Sign Up"], horizontal=True)
email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Submit"):
    if mode == "Login":
        result = firebase_login(email, password)
    else:
        result = firebase_signup(email, password)

    if "error" in result:
        st.error(f"{mode} failed: {result['error']['message']}")
    else:
        # Store session info
        st.session_state["email"] = result["email"]
        st.session_state["uid"] = result["localId"]
        st.session_state["id_token"] = result["idToken"]

        user_id = result["localId"]

        try:
            st.session_state["notes"] = load_user_data(user_id)

            if st.session_state["notes"] != "":
                st.info("📝 Notes loaded.")
            else:
                st.warning("⚠️ No notes found in Firestore.")
        except Exception as e:
            st.error(f"Failed to load notes: {e}")

        st.success(f"{mode} successful! Welcome, {result['email']}")
        time.sleep(1)

        st.switch_page("pages/chat.py")
