# 📝 Prompt Comparison Project

This project evaluates different system prompts (Professional, Creative, and Technical personas) using a Prompt Comparison Rubric.
It helps analyze how effective prompts are in guiding AI responses based on Clarity, Specificity, Consistency, and Effectiveness

# ⚙️ Setup Instructions
# 1️ Clone & Navigate
git clone https://github.com/AmirAliShar/Buildables-AI-Internship.git
cd Buildables-AI-Internship/week2

# 2. Create & Activate a Conda Environment
conda create -n prompt_eval python=3.12 -y
conda activate prompt_eval

# 3. Install Required Packages
pip install langchain langchain_groq langchain_core streamlit python-dotenv

# 4. Add Your API Key

Create a .env file in your project directory:

GROQ_API_KEY=your_GROQ_key_here

# 5. Run the CLI Chat
--> Run with correct file name
python Chatbotwithprompt.py

for streamlit
streamlit run frontend.py




