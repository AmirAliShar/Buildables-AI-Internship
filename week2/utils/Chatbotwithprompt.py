
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import ChatPromptTemplate

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

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

llm =ChatGroq(model ="llama-3.3-70b-versatile")

# Prompts
personas = {
    "Professional": "You are a professional assistant. Respond in a polite, concise, and business-like manner.",
    "Creative": "You are a creative companion. Respond with imagination, storytelling, and playfulness.",
    "Technical": "You are a technical expert. Respond with detailed, step-by-step technical explanations."
}


parsers = StrOutputParser()

def selection(choice: str, llm):
    if choice not in personas:
        print("❌ Invalid choice, defaulting to Professional Assistant.")
        #choice = "Professional"

    # Create a prompt with the chosen system instruction
    prompt = ChatPromptTemplate.from_messages([
        ("system", personas[choice]),
        ("human", "{input}")
    ])

    chain = prompt | llm | parsers
    return chain


def main():
    print("🤖 Groq AI Chatbot (type 'exit' to quit)\n")
    
    choice=input(str("enter the Prompt choice choice"))
    chain = selection(choice, llm)

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Chat ended. Goodbye!")
            break

        try:
            response = chain.invoke(input=user_input)
            print(f"AI: {response}\n")
        except Exception as e:
            print(f"⚠️ Error: {e}")


if __name__ == "__main__":
    main()
