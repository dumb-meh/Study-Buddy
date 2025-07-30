from fastapi import APIRouter, HTTPException, Body
from .task_suggestion import Suggestion
from .task_suggestion import task_suggestion_response

router= APIRouter()
summary= Suggestion()

@router.post("/summary",response_model=task_suggestion_response)
async def get_summary():
    try:
        response=summary.get_suggestion(request_data)
        return task_suggestion_response (response=response)
    
    except Exception as e:
        raise HTTPException (status_code=500, detail=str(e))