# src/config.py
import streamlit as st
import google.generativeai as genai
from utils.sidebar import render_sidebar

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

# Prompt Helpers
SYSTEM_PROMPT = """
You are a highly skilled cybersecurity expert in the 91st Cyber Brigade - Virginia National Guard.
Your mission is to support Cyber Fortress force-on-force operations by generating code/scripts that automate offensive and defensive tasks.
""".strip()

task_context = render_sidebar()
TASK_CONTEXT = f"""
"Language": {task_context["language"]}
"Task Type": {task_context["task_type"]}
"Code Style": {task_context["code_style"]}
"Output Format": {task_context["output_format"]}
"Platform": {task_context["platform"]}
"""

DIRECTIVES = """Respond to the query using these rules:
- Mirror the format of the provided examples: code-only outputs in fenced code blocks.
- Assume every query requires a code-based solution and respond with code only-no comments, explanations, or extra text.
- Rely on the knowledge base and your cybersecurity expertise.
- Do not guess or hallucinate commands, parameters, or syntax. If uncertain, return an empty code block.
""".strip()

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
        "question": "Write a Python function that extracts all IP addresses from a given log file.",
        "answer": "```python\nimport re\n\ndef extract_ips(log_text):\n    return re.findall(r'\\b(?:[0-9]{1,3}\\.){3}[0-9]{1,3}\\b', log_text)\n```"
    }
]

# Streamlit UI
APP_TITLE = "🛡️ Cyber Fortress"
