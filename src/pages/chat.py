from utils.vector_store import *
from utils.chat_helper import *
from utils.embedder import *
from utils.build_prompt import *
from utils.config import *
from utils.config import *
import streamlit as st
import time

st.set_page_config(page_title=APP_TITLE, layout="wide")

# === User Authentication Check ===
if "uid" not in st.session_state:
    st.warning("Please log in to access chat feature.")
    time.sleep(1)
    st.switch_page("login.py")
    st.stop()

st.title(APP_TITLE)
st.markdown(
    "<style>" + open("./style/style.css").read() + "</style>", unsafe_allow_html=True
)

# === Session State Initialization ===
if st.session_state.get("reset_chat", False):
    st.session_state["messages"] = []
    st.session_state["reset_chat"] = False

# Ensure messages is initialized if not set or was cleared above
if "messages" not in st.session_state or not st.session_state["messages"]:
    st.session_state["messages"] = []

# @st.cache_resource(ttl=30)

# Add temp to session state
if "temperature" not in st.session_state:
    st.session_state["temperature"] = 0.3  # preferred default

# === Sidebar: Temperature Slider ===
st.sidebar.markdown("### 🤖 Model Behavior")
st.session_state["temperature"] = st.sidebar.slider(
    "Response Style\n\n(Precision ←→ Creativity)",
    min_value=0.0,
    max_value=1.0,
    value=0.3,
    step=0.05,
    help="Lower = deterministic, higher = creative",
)

st.sidebar.markdown(
    f"**Current Behavior:** {'🎯 Precise' if st.session_state["temperature"] < 0.4 else '🧠 Creative' if st.session_state["temperature"] > 0.6 else '⚖️ Balanced'}"
)

# Previous messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Chat Input
if user_input := st.chat_input("Ask me anything..."):
    if not user_input.strip():
        st.warning("⚠️ Please enter a message before submitting.")
        st.stop()
    st.chat_message("user").write(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

with st.chat_message("assistant"):
    # RAG Search
    # with st.spinner("Thinking..."):
        # RAG: search
    uid = st.session_state["uid"]
    timings = {}
    
    t0 = time.time()
    context_chunks = search_top_k(uid, user_input)
    timings["⚙️ embedder init"] = time.time() - t0

    # Build prompt and generate response
    t1 = time.time()
    prompt = build_prompt(user_input, context_chunks)
    timings["📝 prompt build"] = time.time() - t1
    
    t2 = time.time()
    response = generate_response(prompt, temperature=st.session_state["temperature"])
    timings["🤖 response gen"] = time.time() - t2

    timings["⏱️ total"] = sum(timings.values())
    st.session_state.messages.append({"role": "assistant", "content": response})

    # Source documents
    with st.expander("📚 Relevant Notes"):
        for i, doc in enumerate(context_chunks):
            st.markdown(
                f"""
                <div class=\"source-chunk\">
                    <div class=\"chunk-title\">#{i+1}</div>
                    <div class=\"chunk-body\">{doc.strip()}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

# Display timings
    with st.expander("⏱️ Timings"):
        for k, v in timings.items():
            st.write(f"- **{k}**: {v:.2f} sec")

# New Chat and Logout Buttons
for _ in range(15):
    st.sidebar.write("")

if st.sidebar.button("🆕 New Chat"):
    st.session_state["messages"] = []
    st.rerun()

with st.sidebar:
    if st.button("🔓 Log Out"):
        for key in ["email", "uid", "id_token"]:
            st.session_state.pop(key, None)
        st.rerun()
