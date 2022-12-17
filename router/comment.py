from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from router.schemas import CommentRequestSchema, CommentResponseSchema, CommentResponseWithInfoSchema
from db.database import get_db
from db import db_comment
from typing import List

router = APIRouter(
    prefix='/api/v1/comments',
    tags=['comment']
)


@router.post('', response_model=CommentResponseSchema)
def create(request: CommentRequestSchema, db: Session = Depends(get_db)):
    return db_comment.create(db=db, request=request)

@router.get('/all', response_model=List[CommentResponseSchema])
def get_all_like(db: Session = Depends(get_db)):
    return db_comment.get_all(db)

@router.get('/id/{comment_id}', response_model=CommentResponseWithInfoSchema)
def get_comment_by_id(comment_id: int, db: Session = Depends(get_db)):
    return db_comment.get_comment_by_id(comment_id=comment_id, db=db)

#@router.get('/{post_id}', response_model=CommentResponseSchema)
#def get_post_by_id(post_id: int, db: Session = Depends(get_db)):
#    return db_comment.get_comment_by_post(post_id=post_id, db=db)