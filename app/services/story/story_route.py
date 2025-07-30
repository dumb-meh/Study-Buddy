from fastapi import APIRouter,HTTPException,Body
from .story import Story
from .story_schema import story_response

router= APIRouter()
story=Story()

@router.post("/summary",response_model=story_response)
async def get_summary(request_data: str = Body(..., media_type="text/plain")):
    try:
        response=story.create_story(request_data)
        return story_response (response=response)
    
    except Exception as e:
        raise HTTPException (status_code=500, detail=str(e))