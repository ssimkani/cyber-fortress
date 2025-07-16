import google.generativeai as genai
from utils.config import MODEL_NAME
import streamlit as st
import time

llm = genai.GenerativeModel(MODEL_NAME)

def generate_response(prompt: str) -> str:
    response = llm.generate_content(prompt,
        generation_config=genai.GenerationConfig(temperature=0.3)
)

    # Generate Response
    st.markdown(response.text)

    return response.text
