# Technical Architecture

## System Overview
ResearchRadar is a LangChain-based LLM agent that uses tool integration to fetch and synthesize real-time information from multiple sources using Google Gemini 2.5 Flash.

## Core Components

### 1. Agent Framework
- **Framework**: LangChain Agent with ReAct pattern
- **LLM Provider**: Google Gemini 2.5 Flash
- **Reasoning**: Chain-of-thought reasoning for intelligent tool selection
- **Prompt Strategy**: System prompt with strict formatting rules and query categorization

### 2. Tool Integration
- **Tavily Search API**: Real-time web search for news and industry developments
- **Arxiv API Wrapper** (`ArxivQueryRun`): Academic paper retrieval and summarization
- **Tool Selection Logic**: Automatic categorization into News/Research/Hybrid queries

### 3. Data Processing Pipeline

User Query → Agent Reasoning → Tool Selection → API Calls → Data Synthesis → Structured Output