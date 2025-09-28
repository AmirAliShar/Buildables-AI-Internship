from langchain_community.utilities import ArxivAPIWrapper
from langchain_community.tools import ArxivQueryRun
from langchain_core.tools import tool
from app import vector_retriever
from langchain.tools import Tool
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.tools import tool
   



@tool
def arxiv_tool(query: str) -> str:
    """Fetch one recent AI/tech/education paper from arXiv and return the summary."""
    arxiv_wrapper = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=2000)
    arxiv = ArxivQueryRun(api_wrapper=arxiv_wrapper)
    return arxiv.run(query)

def get_tavily_tool():
    """Return a LangChain Tool for Tavily search (AI, tech, education updates)."""
    tavily_search = TavilySearchResults(max_results=5)
    return Tool(
        name="tavily_search",
        func=tavily_search.run,
        description="Fetch recent AI, technology, or education news and updates."
    )

def dawn_newsTool():
    search = TavilySearchResults(max_results=5)
    
    return Tool(
        name="Dawn_news",
        func=search.run,
        description="Useful for retrieving technology news from Dawn News Pakistan. Use for queries about Pakistani technology news, local tech developments, or Dawn News content."
    )

# this is optional beacause we use the tavily search tool instead of web base 
# @tool
# def Dawn_news(input: str):
#     """
#       Retrieve technology news information from Dawn News Pakistan vector store. 
#       Use this for queries about Pakistani technology news, Dawn News content, 
#        or local tech developments in Pakistan."""
#     retrieved_docs = vector_retriever.invoke(input)  
#     serialized = "\n\n".join(
#         (f"Content: {doc.page_content}") for doc in retrieved_docs
#     )
#     return serialized
