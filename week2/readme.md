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

# 📸 Screenshots

<img width="1919" height="873" alt="Screenshot 2025-08-31 231817" src="https://github.com/user-attachments/assets/a7577ba2-7f64-42d1-b0a2-f158b3f3687e" />

# 📊 Prompt Evaluation Summary

Using the Prompt Comparison Rubric, the same query “Explain photosynthesis simply” was tested across three personas.

| Persona          | Behavior (Observed)                                                               | Score /100 |
| ---------------- | --------------------------------------------------------------------------------- | ---------- |
| **Professional** | Produced a creative-style response instead of concise business tone (misaligned). | 55         |
| **Creative**     | Delivered an imaginative story with a plant named “Phil” (highly aligned).        | 88         |
| **Technical**    | Produced a detailed step-by-step breakdown with chemical equations.               | 95         |


# Insights:

Creative and Technical personas worked as intended.

Professional persona drifted into a creative style → requires a more constrained prompt.

Clearer instructions (e.g., word limit, style guide) improve consistency and effectiveness.

# ✅ Evaluation Criteria

✔️ Functionality – Chat works correctly with persona selection
✔️ Code Quality – Clean, structured, and error-handled
✔️ Prompt Engineering – Demonstrated prompt variations and analysis
✔️ Documentation – Clear setup, screenshots, rubric evaluation, and reflection

# 👨‍💻 Author: Amir Ali
