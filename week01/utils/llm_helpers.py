from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.schema.output_parser import StrOutputParser
import os
from dotenv import load_dotenv

from .tokenizer_helpers import tokenizer_llm


# Load environment variables
load_dotenv()
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

#Instruction 
prompt_ins = """
You are a multi-style AI summarizer. Based on the user's text, you must detect following category:

1. **News Article**
2. **Academic Abstract**
3. **Social Media Post**
4. **Technical Documentation**
5. **Creative Writing**

### Instructions:
- Detect the best-matching format for the user's text.
- Write the summary of the text .
- Do not explain your reasoning; just return the summary of provided text the chosen style.

### User Text:
{Text}

Now generate the summary in the detected format.
"""

# Prompt
prompt = PromptTemplate(
    template=prompt_ins,
    input_variables=["Text"]
)

def Summarizer(text:str,llm_name:str):
    #llm_name = state.llm_name

    if not GROQ_API_KEY:
        raise ValueError("GROQ_API_KEY is missing. Please set it in your .env file.")

    # Initialize LLM
    llm = ChatGroq(model=llm_name, api_key=GROQ_API_KEY)
    parser = StrOutputParser()

    # Create chain
    chain = prompt | llm | parser

    # Run summarization
    #text = state.Text
    response = chain.invoke({"Text": text})

    # Tokenization + cost calculation
    token_info = tokenizer_llm(text)
   


    return {
        "Text": text,
        "response": response,
        "llm_name": llm_name,
        "tokens": token_info["token_count"],
        "cost": token_info["cost"],
    }
