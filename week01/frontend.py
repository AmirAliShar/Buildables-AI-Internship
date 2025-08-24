import streamlit as st
import requests
import time

# Step 1: Setup UI with Streamlit
st.title("🤖 Multi-Purpose AI ChatBot")

# Sidebar for model selection and configuration
with st.sidebar:
    st.write("🛠️ **Configure AI Agent**")
    ALLOWED_MODEL_NAMES = [
        "llama-3.3-70b-versatile", "compound-beta-mini", "deepseek-r1-distill-llama-70b",
        "gemma2-9b-it", "openai/gpt-oss-20b"
    ]
    st.subheader("💬 Choose the Model")
    llm_name = st.selectbox("Select Groq Model:", ALLOWED_MODEL_NAMES)

# Initialize conversation history in session state
if "conversation" not in st.session_state:
    st.session_state.conversation = []

# Display conversation history
st.subheader("💬 **Conversation**")
for message in st.session_state.conversation:
    if message["role"] == "user":
        st.write(f"👨‍🎓 **You:** {message['content']}")
    else:
        st.write(f"🤖 **Agent:** {message['content']}")

# User input
user_query = st.chat_input("Enter your query...")

# API endpoint
API_URL = "http://127.0.0.1:8000/query"
  # Start timer
start_time = time.time()
# Handle user query
if user_query:  # Trigger when the user submits a query
    if user_query.strip():  # Ensure the query is not empty
        with st.spinner("🌐 Thinking..."):
            # Step 2: Connect with backend via URL
            payload = {
                "llm_name": llm_name,
                "Text": user_query,
            }

            # Send request to the backend
            response = requests.post(API_URL, json=payload)

            # Handle response
            if response.status_code == 200:
                response_data = response.json()  
                # Pretty print in debug (optional)
                st.json(response_data)
                end_time = time.time()
                Tolaltime = (end_time - start_time)
                st.write(Tolaltime)


                if "error" in response_data:
                    st.error(response_data["error"])
                else:
                         # Build a formatted agent response with all fields
                    agent_msg = (

                        f"**Original Text:** {response_data['Text']}\n\n"
                        f"**Summary:** {response_data['response']}\n\n"
                        f"**Model:** {response_data['llm_name']}\n\n"
                        f"**Tokens Used:** {response_data['tokens']}\n\n"
                        f"**Cost:** {response_data['cost']}"

                    )
                    
                    # Append user query and agent response to conversation history
                    st.session_state.conversation.append({"role": "user", "content": user_query})
                    st.session_state.conversation.append({"role": "agent", "content": agent_msg})
                 
                   

                    # Rerun the app to update the conversation display
                    st.rerun()

            else:
                st.error("❌ Failed to get a response from the server.")




