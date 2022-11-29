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


@router.get("/id/{info_id}", response_model=InfoResponseSchema)
def get_info_by_id(info_id: int, db: Session = Depends(get_db)):
    return db_info.get_info_by_id(info_id=info_id, db=db)

@router.put("/update/{id}",response_model=UpdateInfoRequestSchema)
def update_info_by_id(id: int,request: UpdateInfoRequestSchema,db: Session = Depends(get_db)):
    return db_info.update_info_by_id(info_id=id,request=request, db=db)