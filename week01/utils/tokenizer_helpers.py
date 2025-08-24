from transformers import AutoTokenizer

def tokenizer_llm(text: str):
    tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
    tokens = tokenizer.tokenize(text)
    token_count = len(tokens)

    
    TOKEN_COSTS = {
        "llama3-8b-8192": 0.000002,   
        "llama-3.3-70b-versatile": 0.0000035
    }

    # Default to llama3-8b if unknown
    cost = token_count * TOKEN_COSTS.get("llama3-8b-8192", 0)

    return {
        "token_count": token_count,
        "cost": cost
    }
