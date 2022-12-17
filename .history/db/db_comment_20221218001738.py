from fastapi import HTTPException, status
from router.schemas import CommentRequestSchema
from sqlalchemy.orm.session import Session
from db.models import DbComment

def create(db: Session, request: CommentRequestSchema) -> DbComment:
    new_comment = DbComment(
        user_id=request.user_id,
        user_name=request.user_name,
        content=request.content,
        info_id=request.info_id,
    )
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment

def get_all(db: Session):
    comment = db.query(DbComment).all()
    if not comment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'comment not found')
    return comment

def get_comment_by_id(comment_id: int, db: Session) -> DbComment:
    comment = db.query(DbComment).filter(DbComment.id == comment_id).first()
    if not comment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Comment with id = {id} not found')
    return comment


# def get_comment_by_post(info_id: int, db: Session) -> list[DbComment]:
#    comment = db.query(DbComment).filter(DbComment.info_id == info_id).first()
#    if not comment:
#        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                            detail=f'Comment with id = {id} not found')
#    return comment