import google.generativeai as genai
from utils.config import MODEL_NAME
import streamlit as st

llm = genai.GenerativeModel(MODEL_NAME)

def generate_response(prompt: str) -> str:
    response = llm.generate_content(prompt,
        generation_config=genai.GenerationConfig(temperature=0.3),
        stream=True)

    response_container = st.empty()
    full_response = ""

    # streaming output
    for chunk in response:
        full_response += chunk.text
        response_container.markdown(full_response + "▌")

    response_container.markdown(full_response)
    return full_response
