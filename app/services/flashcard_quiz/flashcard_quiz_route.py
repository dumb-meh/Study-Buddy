from fastapi import APIRouter, HTTPException, Body
from .flashcard_quiz import FlashCard_Quiz
from .flashcard_quiz_schema import flashcard_quiz_response

router= APIRouter()
summary= FlashCard_Quiz()

@router.post("/flashcard_quiz",response_model=flashcard_quiz_response)
async def generate_flashcard_quiz(request_data: str = Body(..., media_type="text/plain")):
    try:
        response=summary.generate_flashcard_quiz(request_data)
        return flashcard_quiz_response (response=response)
    
    except Exception as e:
        raise HTTPException (status_code=500, detail=str(e))