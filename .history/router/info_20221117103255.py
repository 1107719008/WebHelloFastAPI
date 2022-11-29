from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from router.schemas import InfoRequestSchema, InfoResponseSchema
from db.database import get_db
from db import db_info
from typing import List

router = APIRouter(
    prefix='/api/v1/infos',
    tags=['infos']
)


@router.post('', response_model=InfoResponseSchema)
def create(request: InfoRequestSchema, db: Session = Depends(get_db)):
    return db_info.create(db=db, request=request)


@router.get('/all', response_model=List[InfoResponseSchema])
def get_all_info(db: Session = Depends(get_db)):
    return db_info.get_all(db)


@router.get("/{id}", response_model=List[InfoResponseSchema])
def get_info_by_id(id: int, db: Session = Depends(get_db)):
    return db_info.get_info_by_id(info_id=id, db=db)