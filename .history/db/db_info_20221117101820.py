from fastapi import HTTPException, status
from router.schemas import InfoRequestSchema
from sqlalchemy import func
from sqlalchemy.orm.session import Session
#from .products_feed import products
from db.models import DbHomework



def create(db: Session, request: InfoRequestSchema) -> DbHomework:
    new_product = DbHomework(
        title=request.title,
        name=request.name,
        description=request.description,
        description_long=request.description_long
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


def get_all(db: Session) -> list[DbHomework]:
    return db.query(DbHomework).all()


def get_info_by_id(info_id: int, db: Session) -> DbHomework:
    info = db.query(DbHomework).filter(DbHomework.id == info_id).first()
    if not info:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Info with id = {info_id} not found')
    return info


