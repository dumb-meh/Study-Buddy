from fastapi import APIRouter,HTTPException,Body
from .mnemonic import Mnemonic
from .mnemonic_schema import mnemonic_reponse

router= APIRouter()
mnemonic=Mnemonic()

@router.post("/mnemonic",response_model=mnemonic_reponse)
async def get_mnemonic(request_data: str = Body(..., media_type="text/plain")):
    try:
        response=mnemonic.get_mnemonic(request_data)
        return mnemonic_reponse (response=response)
    
    except Exception as e:
        raise HTTPException (status_code=500, detail=str(e))