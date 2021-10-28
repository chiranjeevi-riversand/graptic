from fastapi import APIRouter, HTTPException
from typing import List

from ticketService.app.api.model import TicOut, TicIn

tic = APIRouter()

@tic.post('/', response_model=TicOut, status_code=201)
async def create_tic(payload: TicIn):
    tic_id = 12344

    response = {
        'id': tic_id,
        **payload.dict()
    }

    return response

@tic.get('/{id}/', response_model=TicOut)
async def get_tic(id: int):
    if not id:
        raise HTTPException(status_code=404, detail="Cast not found")

    response = {
        'id': id,
        "desc" : " mydesc "
    }
    return response