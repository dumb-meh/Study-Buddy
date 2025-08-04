from pydantic import BaseModel
from typing import Dict, Any, Optional

class affirmation_request(BaseModel):
    past_affirmations: Dict[str, Any]
    user_mood: Optional[str] = None
class affirmation_response:
    story:str

