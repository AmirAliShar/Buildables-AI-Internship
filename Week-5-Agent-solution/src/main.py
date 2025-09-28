import streamlit as st
from agent import agent_executor  # import agent executor

st.set_page_config(page_title="ResearchRadar AI Agent", page_icon="🤖", layout="wide")

st.title("🤖 ResearchRadar AI Agent")
st.markdown("Ask questions about **AI news, research papers, Dawn News, or technology updates** and let the agent find answers.")

# Initialize session state for conversation history
if "conversation" not in st.session_state:
    st.session_state.conversation = []
if "show_debug" not in st.session_state:
    st.session_state.show_debug = False

# Sidebar
st.sidebar.header("Settings")
st.session_state.show_debug = st.sidebar.checkbox("Show Agent Reasoning", value=False)

# Clear conversation button
if st.sidebar.button("Clear Conversation"):
    st.session_state.conversation = []
    st.rerun()

# Display conversation history
st.subheader("💬 Conversation History")

for i, exchange in enumerate(st.session_state.conversation):
    with st.chat_message("user"):
        st.write(f"**You:** {exchange['question']}")
    
    with st.chat_message("assistant"):
        st.write(f"**ResearchRadar:** {exchange['answer']}")
        
        # Show debug info if enabled
        if st.session_state.show_debug and exchange.get('debug_info'):
            with st.expander("🔍 Agent Reasoning Details"):
                st.json(exchange['debug_info'], expanded=False)
    
    st.markdown("---")

# Current question input
user_input = st.chat_input("Enter your question about AI news, research, or Dawn News...")

if user_input:
    # Add user message to conversation
    st.session_state.conversation.append({
        "question": user_input,
        "answer": "",
        "debug_info": None
    })
    
    # Display user message immediately
    with st.chat_message("user"):
        st.write(f"**You:** {user_input}")
    
    # Get agent response
    with st.chat_message("assistant"):
        with st.spinner("ResearchRadar is searching for answers..."):
            try:
                result = agent_executor.invoke({"input": user_input})
                
                # Update the conversation with answer
                st.session_state.conversation[-1]["answer"] = result["output"]
                st.session_state.conversation[-1]["debug_info"] = result
                
                # Display the answer
                st.write(f"**ResearchRadar:** {result['output']}")
                
                # Show debug info if enabled
                if st.session_state.show_debug:
                    with st.expander("🔍 Agent Reasoning Details"):
                        st.json(result, expanded=False)
                        
            except Exception as e:
                error_msg = f"Sorry, I encountered an error: {str(e)}"
                st.session_state.conversation[-1]["answer"] = error_msg
                st.error(error_msg)

# Sidebar information
st.sidebar.markdown("---")
st.sidebar.subheader("💡 Example Queries")

st.sidebar.markdown("**🤖 AI & Research Queries**")
st.sidebar.markdown("""
- "Latest AI news from past week"
- "Recent papers about LLM agents"  
- "Education technology updates and research"
- "Microsoft AI projects news"
""")

st.sidebar.markdown("**🔍 Hybrid Queries**")
st.sidebar.markdown("""
- "AI news and related research papers"
- "Technology trends in Pakistan and globally"
- "Education developments in Pakistan and research"
""")

st.sidebar.markdown("**📰 Dawn News Queries**")
st.sidebar.markdown("""
- "Latest Pakistan technology news from Dawn"
- "Dawn News updates on AI developments"
- "Education policy news from Dawn"
- "Recent business news from Dawn News"
""")

st.sidebar.markdown("---")
st.sidebar.subheader("🔧 Tools Available")
st.sidebar.markdown("""
- **📰 Dawn News Search** (WebBaseLoader and tavily search)
- **🌐 Global News Search** (Tavily API) 
- **📚 Research Papers** (Arxiv API)
- **🤖 AI Reasoning** (Google Gemini)
""")

st.sidebar.markdown("---")
st.sidebar.subheader("ℹ️ About")
st.sidebar.markdown("""
ResearchRadar automatically categorizes your query and uses the appropriate tools:
- **Dawn News queries**: Pakistan-specific news
- **Technology/AI queries**: Global news + research
- **Hybrid queries**: Combines multiple sources
""")
