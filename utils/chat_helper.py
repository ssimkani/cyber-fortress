import google.generativeai as genai
from utils.config import MODEL_NAME
import streamlit as st
import time

llm = genai.GenerativeModel(MODEL_NAME)

def generate_response(prompt: str, temperature) -> str:
    response = llm.generate_content(prompt,
        generation_config=genai.GenerationConfig(temperature=temperature),
        stream=True)
    # response_text = response.text.strip()

    # # streaming output
    # with response_container:
    #     # for i in range(1, len(response_text) + 1):
    #     #     st.markdown(response_text[:i] + "▌")
    #     #     time.sleep(0.001)
    #     for chunk in response:
    #         st.markdown(chunk.text)
    # return response_text
    
    response_container = st.empty()
    full_response = ""

    # streaming output
    for chunk in response:
        full_response += chunk.text
        response_container.markdown(full_response + "▌")

    response_container.markdown(full_response)
    return full_response
