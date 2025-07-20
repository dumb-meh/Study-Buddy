from pydantic import BaseModel

class summary_request(BaseModel):
    text:str

class summary_response(BaseModel):
    response:str
