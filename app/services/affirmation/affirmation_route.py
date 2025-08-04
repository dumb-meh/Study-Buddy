from fastapi import APIRouter,HTTPException,Body
from .affirmation import Affirmation
from .affirmation_schema import affirmation_response

router= APIRouter()
story= Affirmation()

@router.post("/affirmation",response_model=affirmation_response)
async def get_affirmation(request_data: str = Body(..., media_type="text/plain")):
    try:
        response=story.create_story(request_data)
        return affirmation_response (response=response)
    
    except Exception as e:
        raise HTTPException (status_code=500, detail=str(e))