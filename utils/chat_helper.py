import google.generativeai as genai
from utils.config import MODEL_NAME
import streamlit as st
import time

llm = genai.GenerativeModel(MODEL_NAME)

def generate_response(prompt: str) -> str:
    response = llm.generate_content(prompt,
        generation_config=genai.GenerationConfig(temperature=0.3)
)

    # Simulate response streaming
    response_container = st.empty()
    with response_container:
        for i in range(1, len(response) + 1):
            st.markdown(response[:i] + "▌")
            time.sleep(0.001)
        st.markdown(response)

    return response
