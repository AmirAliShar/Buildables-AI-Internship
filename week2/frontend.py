import os
from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import ChatPromptTemplate

# Load API key
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    st.error("Please set GROQ_API_KEY in your .env file")
    st.stop()

# LLM
llm = ChatGroq(model="llama-3.3-70b-versatile")

# Personas
personas = {
    "Professional": "You are a professional assistant. Respond in a polite, concise, and business-like manner.",
    "Creative": "You are a creative companion. Respond with imagination, storytelling, and playfulness.",
    "Technical": "You are a technical expert. Respond with detailed, step-by-step technical explanations."
}

parser = StrOutputParser()

def build_chain(choice: str):
    """Create a chain with selected persona"""
    if choice not in personas:
        choice = "Professional"
    prompt = ChatPromptTemplate.from_messages([
        ("system", personas[choice]),
        ("human", "{input}")
    ])
    chain = prompt | llm | parser
    return chain

# -------------------- Streamlit UI --------------------

st.set_page_config(page_title="Groq AI Chatbot", page_icon="🤖", layout="centered")

st.title("🤖 Groq AI Chatbot")
st.write("Select a persona and chat with the AI. Type below:")

# Sidebar for persona selection
persona_choice = st.sidebar.selectbox(
    "Choose Persona",
    options=list(personas.keys()),
    index=0
)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "chain" not in st.session_state or st.session_state.get("persona") != persona_choice:
    st.session_state.chain = build_chain(persona_choice)
    st.session_state.persona = persona_choice
    st.session_state.messages = []  # reset chat when persona changes

# Chat history display
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.chat_message("user").markdown(msg["content"])
    else:
        st.chat_message("assistant").markdown(msg["content"])

# Chat input
if user_input := st.chat_input("Type your message..."):
    # Append user input
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").markdown(user_input)

    try:
        response = st.session_state.chain.invoke({"input": user_input})
    except Exception as e:
        response = f"⚠️ Error: {e}"

    # Append response
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.chat_message("assistant").markdown(response)

if st.sidebar.button("Export Chat"):
    chat_text = "\n".join([f"{m['role']}: {m['content']}" for m in st.session_state.messages])
    st.sidebar.download_button("Download Chat", chat_text, file_name="chat_history.txt")
