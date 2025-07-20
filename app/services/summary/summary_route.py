from fastapi import APIRouter, HTTPException, Body
from .summary import Summary
from .summary_schema import summary_response

router= APIRouter()
summary= Summary()

@router.post("/summary",response_model=summary_response)
async def get_summary(request_data: str = Body(..., media_type="text/plain")):
    try:
        response=summary.get_summary(request_data)
        return summary_response (response=response)
    
    except Exception as e:
        raise HTTPException (status_code=500, detail=str(e))