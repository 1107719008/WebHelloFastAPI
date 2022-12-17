from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from router.schemas import LikeRequestSchema, LikeResponseSchema
from db.database import get_db
from db import db_like
from typing import List

router = APIRouter(
    prefix='/api/v1/like',
    tags=['like']
)


@router.post('', response_model=LikeResponseSchema)
async def create(request: LikeRequestSchema, db: Session = Depends(get_db)):
    return db_like.create(db=db, request=request)


@router.get('/all', response_model=List[LikeResponseSchema])
def get_all_like(db: Session = Depends(get_db)):
    return db_like.get_all(db)


#@router.get('/id/{like_id}', response_model=List[LikeResponseWithProductSchema])
#def get_like_by_id(like_id: int, db: Session = Depends(get_db)):
#    return db_like.get_like_by_id(like_id=like_id, db=db)