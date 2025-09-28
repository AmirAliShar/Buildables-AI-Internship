# ResearchRadar AI Agent - Intelligent News & Research Assistant
## Problem Statement
Professionals in AI, technology, and academia face significant information overload, spending 30-60 minutes daily manually searching across multiple sources like Dawn News, global tech news, and research papers. This fragmented approach leads to missed critical updates, inconsistent formatting, and productivity bottlenecks for researchers, entrepreneurs, and students who need to stay current with fast-moving developments.

## Solution Architecture
ResearchRadar is an intelligent LLM agent built with LangChain that automatically fetches and synthesizes information from multiple sources. The system uses Google Gemini 2.5 Flash for reasoning and combines Tavily Search for real-time news with Arxiv API for research papers. A specialized Dawn News tool provides Pakistan-specific technology coverage through targeted web searches.

## Technical Stack:

Framework: LangChain with ReAct agent pattern

LLM: Google Gemini 2.5 Flash

Tools: Tavily Search API, Arxiv API, Custom Dawn News search

Interface: Streamlit web application

Features: Conversation history, smart query categorization, structured output

## Setup Instructions
Prerequisites
Python 3.8+

Tavily API key

Google Gemini API key

Installation
bash
## Clone the repository
git clone https://github.com/AmirAliShar/Buildables-AI-Internship.git
cd Week-5-Agent-solution

## Install dependencies
pip install -r requirements.txt

## Set up environment variables
cp .env.example .env
## Add your API keys to .env:
## TAVILY_API_KEY=your_tavily_key
## GOOGLE_API_KEY=your_gemini_key

## Running the Application

streamlit run src/main.py

## Demo Video
https://youtu.be/tmrrjsJjv3Q

# Usage Examples
## News Queries
"Latest AI news from Pakistan and globally"

"Technology developments from Dawn News"

"Recent updates from OpenAI and Google"

## Research Queries
"Recent papers about large language models"

"AI in healthcare research"

"Computer vision breakthroughs"

## Hybrid Queries
"Education technology news and related research"

"AI developments with supporting academic papers"

"Pakistan tech scene and global trends"

# Technical Challenges
## 1. Intelligent Tool Selection
Problem: Agent incorrectly choosing tools for different query types
Solution: Advanced prompt engineering with explicit query categorization rules and tool selection logic

## 2. Consistent Output Formatting
Problem: Inconsistent response structures across different queries
Solution: Strict formatting rules in system prompt with word limits and section organization

## 3. Dawn News Integration
Problem: Providing relevant Pakistan-specific technology coverage
Solution: Custom Tavily search tool optimized for Dawn News technology content with regional context awareness

## 4. Error Handling & Reliability
Problem: API failures and timeout issues
Solution: Robust error handling, retry mechanisms, and graceful fallback responses

# Impact & Results
Time Efficiency
Before: 30-60 minutes daily manual research

After: Under 60 seconds automated synthesis

Improvement: 97% reduction in information gathering time

Quality Improvements
Comprehensive coverage across news and research

Structured, scannable output format

Source verification and proper attribution

Reduced risk of missing critical updates

Scalability
Supports individual users and teams

Extensible architecture for new data sources

Customizable query types and output formats

# Future Improvements
Immediate Enhancements
Twitter/X integration for real-time developer updates

GitHub trends tracking for open-source developments

Email digest generation for daily summaries

Medium-term Goals
Personalized news preferences and topics

Team collaboration and sharing features

Mobile application development

Long-term Vision
Predictive trend analysis and insights

Multi-language support

Enterprise knowledge management integration

<img width="1915" height="859" alt="image" src="https://github.com/user-attachments/assets/8a7688ca-668d-4b47-96fb-9dbb54debea2" />
