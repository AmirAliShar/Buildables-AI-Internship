#This is a Optional because we use the tavliy search instead of web base

from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
import bs4
from langchain_community.document_loaders import WebBaseLoader
embeddings = OllamaEmbeddings(model="nomic-embed-text")

vector_store = Chroma(
    collection_name="example_collection",
    embedding_function=embeddings,
    persist_directory="./chroma_langchain_db",  # Where to save data locally, remove if not necessary
)

# Load all content first
bs4_strainer = bs4.SoupStrainer(["story__content ",'article'])

loader = WebBaseLoader(
    web_paths=("https://www.dawn.com/tech",),
    bs_kwargs={"parse_only": bs4_strainer},
)
docs = loader.load()

from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,  # chunk size (characters)
    chunk_overlap=20,  # chunk overlap (characters)
    add_start_index=True,  # track index in original document
)
all_splits = text_splitter.split_documents(docs)


all_splits = text_splitter.split_documents(docs)

def vector_retrievers():
    """Add documents into the vector store"""
    document_ids = vector_store.add_documents(documents=all_splits)
    return document_ids

# ✅ Create a retriever object for searching
vector_retriever = vector_store.as_retriever(search_kwargs={"k": 2})