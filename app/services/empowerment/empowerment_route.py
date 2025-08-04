from fastapi import APIRouter,HTTPException,Body
from .empowerment import Empowerment
from .empowerment_schema import empowerment_response


router= APIRouter()
empower= Empowerment()

@router.get("/empowerment",response_model=empowerment_response)
async def get_empowerment_tasks(request_data: str = Body(..., media_type="text/plain")):
    try:
        response=empower.empowerment_tasks (request_data)
        return empowerment_response (response=response)
    
    except Exception as e:
        raise HTTPException (status_code=500, detail=str(e))