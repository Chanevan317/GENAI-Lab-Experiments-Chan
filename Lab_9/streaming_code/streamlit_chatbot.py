from langchain_groq import ChatGroq
import streamlit as st

GROQ_API_KEY = "YOUR_GROQ_API_KEY"  # Replace with your actual API key

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    api_key=GROQ_API_KEY
)

st.title("Simple AI Chatbot")

sawal = st.text_input("USER:", key="user_question")

if sawal:
    response = llm.invoke(sawal)
    st.write(response.content)