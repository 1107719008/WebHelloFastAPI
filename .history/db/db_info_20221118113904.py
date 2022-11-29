from fastapi import HTTPException, status
from router.schemas import InfoRequestSchema,UpdateInfoRequestSchema,UpdateInfoResponseSchema
from sqlalchemy import func
from sqlalchemy.orm.session import Session
#from .products_feed import products
from db.models import DbHomework



def create(db: Session, request: InfoRequestSchema) -> DbHomework:
    info_product = DbHomework(
        title = request.title,
        username = request.username,
        content = request.content,
        contentlong = request.contentlong,
        password = request.password,
       
    )
    db.add(info_product)
    db.commit()
    db.refresh(info_product)
    return info_product


def get_all(db: Session) -> list[DbHomework]:
    return db.query(DbHomework).all()


def get_info_by_id(info_id: int, db: Session) -> DbHomework:
    info = db.query(DbHomework).filter(DbHomework.id == info_id).first()
    if not info:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Info with id = {info_id} not found')
    return info

def update_info_by_id(id: int,request:UpdateInfoRequestSchema, db: Session)-> DbHomework:
    updated_info = db.query(DbHomework).filter(DbHomework.id == id)
    updated_info.update({
        DbHomework.title:request.title,
        DbHomework.username:request.username,
        DbHomework.content:request.content,
        DbHomework.contentlong:request.content,
        DbHomework.password:request.password
    })
    
    return {
       'title': updated_info.title,
        'username': updated_info.username,
        'content': updated_info.content,
        'contentlong': updated_info.contentlong,
        'password': updated_info.password,
    }
