# chat.py or sidebar.py
import streamlit as st

def render_sidebar():
    st.markdown("*Cyber Fortress Code Generator*")

    # Output language selector
    language = st.selectbox("💻 Output Language", ["bash", "python", "powershell", "go", "javascript", "c++", "json", "yaml"])

    # Task type
    task_type = st.radio("🧪 Task Type", ["General-purpose", "Exploitation", "Hardening", "Automation"])

    # Code style
    code_style = st.selectbox("📝 Code Style", ["Raw", "Minimal Comments", "Verbose"])

    # Output format
    output_format = st.radio("📦 Output Format", ["Single Function", "Full Script", "One-Liner"], horizontal=True)

    # Execution platform
    platform = st.selectbox("🖥️ Platform", ["Linux", "Windows", "macOS", "AWS CloudShell"])

    # Expandable description
    with st.expander("## 🤖 What This Chatbot Does"):
        st.markdown(
        """
        **Specializes in**:
        - Cybersecurity reasoning and automation
        - AWS infrastructure & scripting
        - Cyber Fortress operations and technical command generation

        It uses a Retrieval-Augmented Generation (RAG) system with Gemini 2.5 Flash to provide accurate, context-aware responses.  
        ⚠️ All responses are in **code/script-only format**—no explanations or fluff.
        """
    )

    # Reset button
    if st.button("🔄 Reset Session"):
        st.session_state["messages"] = []
        st.rerun()

    if st.button("🔓 Log Out"):
        st.session_state["reset_chat"] = True
        for key in ["email", "uid", "id_token"]:
            st.session_state.pop(key, None)
        st.rerun()

    # Return all values for use in the prompt
    return {
        "language": language,
        "task_type": task_type,
        "code_style": code_style,
        "output_format": output_format,
        "platform": platform,
    }
