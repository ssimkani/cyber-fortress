# src/config.py
import streamlit as st
import google.generativeai as genai

# Embedding Model
EMBEDDING_MODEL = "models/text-embedding-004"

# GEMINI
GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
MODEL_NAME = "gemini-2.5-flash"

genai.configure(api_key=GEMINI_API_KEY)

# FIREBASE
FIREBASE_API_KEY = st.secrets["FIREBASE_API_KEY"]
FIREBASE_CRED = "firebase_cred.json"

# PINECONE
PINECONE_API_KEY = st.secrets["PINECONE_API_KEY"]
PINECONE_INDEX_NAME = "cyber-fortress"

# Chunking Settings
CHUNK_SIZE = 1500
CHUNK_OVERLAP = 150
NUM_CHUNKS = 4

# System Prompt
SYSTEM_PROMPT = """
You are a highly skilled cybersecurity expert in the 91st Cyber Brigade - Virginia National Guard.
Your mission is to support Cyber Fortress force-on-force operations by generating scripts that automate offensive and defensive tasks.

Answer the query using these guidelines:
- Mirror the format of the provided examples: code-only outputs in fenced code blocks.
- Rely on the knowledge base and your cybersecurity expertise.
- Output only the code/script(s)—no comments, explanations, or extra text.
- Generate accurate responses and avoid Hallucinations.
"""

EXAMPLES = [
    {
        "question": "Generate a Bash script that finds all SUID binaries on Linux.",
        "answer": "```bash\nfind / -perm -4000 -type f 2>/dev/null\n```"
    },
    {
        "question": "Write a PowerShell script to list all local administrators.",
        "answer": "```powershell\nGet-LocalGroupMember -Group 'Administrators'\n```"
    },
    {
        "question": "Create a Bash script to monitor SSH login attempts from /var/log/auth.log.",
        "answer": "```bash\ngrep 'sshd' /var/log/auth.log | grep 'Failed'\n```"
    }
]

# Streamlit UI
APP_TITLE = "🛡️ Cyber Fortress"
