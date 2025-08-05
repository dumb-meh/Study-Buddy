from pydantic import BaseModel
from typing import Dict,List, Any

class empowerment_response(BaseModel):
    tasks: Dict[str, Any]