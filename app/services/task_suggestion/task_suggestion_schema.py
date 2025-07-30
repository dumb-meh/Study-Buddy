from pydantic import BaseModel
from typing import Dict,List, Any

class task_suggestion_request(BaseModel):
    tasks: Dict[str, Any]

class task_suggestion_response(BaseModel):
    tasks: Dict[str, Any]