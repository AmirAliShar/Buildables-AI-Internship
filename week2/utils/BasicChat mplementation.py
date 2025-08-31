
from langchain_groq import ChatGroq
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

#For llm caches
from langchain_core.caches import InMemoryCache
from langchain_core.globals import set_llm_cache
set_llm_cache(InMemoryCache())

# Load API key from .env file
# Must have the API key of model (I am using the Groq API key)
import os
from dotenv import load_dotenv
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("Please set GROQ_API_KEY in your .env file")

# Initialize Groq model via LangChain
llm = ChatGroq(
    groq_api_key=GROQ_API_KEY, #Api key
    model="llama-3.1-8b-instant"  # Model Name
)

# Conversation memory (stores context automatically)
memory = ConversationBufferMemory()

# Create a conversation chain
conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=False
)

def main():
    print("🤖 Groq AI Chatbot (type 'exit' to quit)\n")
    
    while True: 
        user_input = input("You: Ask the query... ")
        if user_input.lower() in ["exit", "quit"]:
            print("Chat ended. Goodbye!")
            break
        
        try:
            response = conversation.predict(input=user_input)
            print(f"AI: {response}\n")
        except Exception as e:
            print(f"⚠️ Error: {e}")

if __name__ == "__main__":
    main()
