from fastapi import APIRouter, HTTPException, Body
from .task_suggestion import TaskSuggestion
from .task_suggestion_schema import task_suggestion_request,task_suggestion_response

router= APIRouter()
summary= TaskSuggestion()

@router.post("/suggestion",response_model=task_suggestion_response)
async def get_summary():
    try:
        response=summary.get_suggestion(request=task_suggestion_request)
        return task_suggestion_response (response=response)
    
    except Exception as e:
        raise HTTPException (status_code=500, detail=str(e))