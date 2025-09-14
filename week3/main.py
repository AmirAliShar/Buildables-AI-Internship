from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import ChatPromptTemplate
from langgraph.graph import StateGraph, START, END
from utils.schema import State, InputState

# LLM cache
from langchain_core.caches import InMemoryCache
from langchain_core.globals import set_llm_cache
set_llm_cache(InMemoryCache())

import os
from dotenv import load_dotenv
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("Please set GROQ_API_KEY in your .env file")

llm = ChatGroq(model="llama-3.3-70b-versatile")

def simpleHi(state: InputState):
    
    return {"response": "Hello! how can I help you today?"}

def ZeroShot(state: InputState):
    q = state.query
    prompt_text = f"""You are an AI reasoning assistant.
Solve the following problem directly.
Do not explain steps. Do not show reasoning.

Question: {q}

Answer:"""
    response = llm.invoke(prompt_text).content
    return {"response": response}

def FewShot(state: InputState):
    q = state.query
    prompt_text = f'''You are an AI reasoning assistant.
Look at the examples and follow the same style to solve the new problem.

Examples:
Question: If John has 2 apples and buys 3 more, how many does he have?
Answer: 5

Question: What is 12 + 8?
Answer: 20

Now solve this problem in the same way:

Question: {q}
Answer:'''
    response = llm.invoke(prompt_text).content
    return {"response": response}

def COT(state: InputState):
    q = state.query
    prompt_text = f'''You are an AI reasoning assistant.
Solve this problem carefully.
Think step by step and show your reasoning before giving the final answer.

Question: {q}

Step-by-step reasoning:

Final Answer:'''
    response = llm.invoke(prompt_text).content
    return {"response": response}

def conditional_condition(state: InputState):
    #return node IDs exactly as added below
    if state.prompt == "ZeroShot":
        return "zero"
    elif state.prompt == "FewShot":
        return "few"
    else:
        return "cot"

workflow = StateGraph(State)
workflow.add_node("simple", simpleHi)
workflow.add_node("zero", ZeroShot)
workflow.add_node("few", FewShot)
workflow.add_node("cot", COT)

workflow.add_edge(START, "simple")
workflow.add_conditional_edges("simple", conditional_condition)
workflow.add_edge("zero", END)
workflow.add_edge("few", END)
workflow.add_edge("cot", END)

graph = workflow.compile()


res = graph.invoke({"query": "Translate 'Good morning, how are you?' into French", "prompt": "COT"})
print(res["response"])
