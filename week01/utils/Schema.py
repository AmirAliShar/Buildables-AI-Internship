from pydantic import BaseModel
# Request schema
class InputState(BaseModel):
    Text: str ="Artificial Intelligence is transforming industries by enabling automation and decision-making." 
    llm_name:str= "compound-beta-mini"

# Response schema
class ResState(BaseModel):
    Text: str
    response: str
    tokens: int
    cost: float
    llm_name:str