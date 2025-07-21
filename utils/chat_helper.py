import google.generativeai as genai
from utils.config import MODEL_NAME
import streamlit as st
import time

@st.cache_resource
def load_llm():
    return genai.GenerativeModel(MODEL_NAME)

def generate_response(prompt: str) -> str:
    llm = load_llm()
    response = llm.generate_content(prompt,
        generation_config=genai.GenerationConfig(temperature=0.3)
)
    return response.text
