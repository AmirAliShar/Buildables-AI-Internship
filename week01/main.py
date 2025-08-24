from fastapi import FastAPI, HTTPException
import uvicorn
from utils.Schema import InputState,ResState
from utils.llm_helpers import Summarizer
# Allowed AI Models
ALLOWED_MODEL_NAMES = [
    "llama-3.3-70b-versatile","compound-beta-mini","deepseek-r1-distill-llama-70b",
    "gemma2-9b-it", "openai/gpt-oss-20b"
]

app = FastAPI(title="AI Summarizer with Token Tracking")

@app.post("/query", response_model=ResState)
def query_agent(request: InputState):
    if request.llm_name not in ALLOWED_MODEL_NAMES:
        return {"error":"Invalid model name"}

    try:
        result = Summarizer(request.Text,request.llm_name)   
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing query: {str(e)}")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
