from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, START, END
from pydantic import BaseModel, Field
from typing import Literal, Annotated
from langchain_core.caches import InMemoryCache
from langchain_core.globals import set_llm_cache
import os
from dotenv import load_dotenv
from langgraph.checkpoint.memory import InMemorySaver
# LLM cache
set_llm_cache(InMemoryCache())

# Load API key
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("Please set GROQ_API_KEY in your .env file")
  
# ---------------- Models ---------------- #
class InputState(BaseModel):
    LLM: Literal["openai", "gemma"] = Field(description="Select the LLM")
    query: Annotated[str, Field(description="Question of the human")]
    prompt: Literal["QA", "Summarize"] = Field(description="Select QA or Summarize")
    temperature:Annotated[float,Field(description="Temperature for creativity")]
    

class State(BaseModel):
    query: str
    response: str = ""
    prompt: Literal["QA", "Summarize"]
    LLM: object = None  # will store actual LLM object
    temperature:float
    

# ---------------- Node Functions ---------------- #
def LLMSelection(state: InputState):
    if state.LLM == "gemma":
        llm = ChatGroq(model="gemma2-9b-it",temperature=state.temperature,)
    elif state.LLM == "openai":
        llm = ChatGroq(model="openai/gpt-oss-20b",temperature=state.temperature)
    else:
        raise ValueError("Invalid LLM selection")

    return {"LLM": llm, "query": state.query, "prompt": state.prompt}

def QA(state: State):
    question = state.query
    llm = state.LLM
    prompt_text = f"""You are an AI Question and Answering assistant.
Answer the following question directly.
Do not explain steps. Do not explain.

Question: {question}

Please give the answer as:
Based on the article below, \[question]?
Article : answer 

"""
    response = llm.invoke(prompt_text).content
    return {"response": response}

def Summarize(state: State):
    text = state.query
    llm = state.LLM
    prompt_text = f"""You are an AI Summarizer assistant.
Summarize the following text carefully upto 3 to 4 lines.

Text: {text}

Summary:"""
    response = llm.invoke(prompt_text).content
    return {"response": response}

def conditional_condition(state: State):
    if state.prompt == "QA":
        return "qa"
    elif state.prompt == "Summarize":
        return "summarizer"
    else:
        raise ValueError("Invalid prompt type")

# ---------------- Workflow ---------------- #
workflow = StateGraph(State)
workflow.add_node("simple", LLMSelection)
workflow.add_node("qa", QA)
workflow.add_node("summarizer", Summarize)

workflow.add_edge(START, "simple")
workflow.add_conditional_edges("simple", conditional_condition)
workflow.add_edge("qa", END)
workflow.add_edge("summarizer", END)

checkpointer=InMemorySaver()
graph = workflow.compile(checkpointer=checkpointer)

def word_count(text):
    word=text.split()
    words=len(word)
    return words

#Article news
Article ="""
YouTube is giving creators new ways to monetize, with brand deals and through the YouTube Shopping program, which lets creators earn money by featuring and tagging products in their content. YouTube will also now allow creators to swap out brand sponsorships in long-form videos.

Creators can also take advantage of auto timestamps for product tags, auto tagging for eligible items mentioned in videos, and a new brand link feature for Shorts. An AI-powered system will help identify the optimal moment a product is mentioned and automatically display the product tag at that time.

Shorts creators will soon be able to add a link to a brand’s site specifically for brand deals, and YouTube will proactively suggest creators who may be a good fit for brands in its creator partnerships hub.
"""
print("Orginal article total words")
word_count(Article)

# temperature = 0.1 (Please You can change the temperature value like as 0.1,0.7 and 1.0)
config={"configurable":{"thread_id":"1"}}
res = graph.invoke({"query": Article, "prompt": "Summarize", "LLM": "gemma","temperature":0.1},config=config)
result=res["response"] 
print(result)
word_count(result)


# For questions
Result = graph.invoke({
    "LLM": "openai", 
    "query": "Is YouTube expanding monetization ?", 
    "prompt": "QA","temprature":0.7
},config=config)
print("Response:", Result["response"])
  