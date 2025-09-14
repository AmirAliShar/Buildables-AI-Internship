from pydantic import BaseModel,Field
from typing import Annotated,Literal

class InputState(BaseModel):
    query:Annotated[str, Field(description="Question of the human")]
    prompt:Literal["ZeroShot","FewShot","COT"] =Field(description="According to question prompt selection")
    

class State(BaseModel):
    query:Annotated[str, Field(description="Question of the human")]
    response:str
    prompt:Literal["ZeroShot","FewShot","COT"] =Field(description="According to question prompt selection")
    
