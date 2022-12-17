from .database import Base
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey


class DbProduct(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True, index=True)
    category = Column(String(30), nullable=False)
    name = Column(String(30), nullable=False)
    sku = Column(String(30))
    price = Column(Integer, nullable=False)
    image = Column(String(100), nullable=False)
    description = Column(String(100), nullable=False)
    description_long = Column(String(255), nullable=True)
    currency = Column(String(10))
    countInStock = Column(Integer, nullable=False)
    owner_id = Column(Integer, ForeignKey('user.id'))
    owner = relationship('DbUser', back_populates='created_products')

#use for hw below----------------------------------------------------------------
class DbUser(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(30), unique=True, nullable=False)
    email = Column(String(30), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    is_admin = Column(Boolean, default=False, nullable=True)
    #created_products = relationship('DbProduct', back_populates='owner')
    #likes = relationship('DbLike', back_populates='liked_owner')
    #comments = relationship('DbComment', back_populates='commented_owner')

class DbHomework(Base):
    __tablename__ = 'hw'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    username = Column(String)
    content = Column(String)
    contentlong = Column(String)
    like_count = Column(Integer)
    comment_count = Column(Integer)
    owner_id = Column(Integer, ForeignKey('user.id'))
    #owner = relationship('DbUser', back_populates='created_posts')
    likeby = relationship('DbLike', back_populates ='liked_post')
    commentby = relationship('DbComment', back_populates ='commented_post')

class DbLike(Base):
    __tablename__ = 'like'
    id = Column(Integer, primary_key=True, index=True)
    info_id = Column(Integer, ForeignKey('hw.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    user_name = Column(String(30), unique=True, nullable=False)
    liked_post = relationship('DbHomework', back_populates='likeby')
    #liked_owner = relationship('DbUser', back_populates='likes')

class DbComment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String(255),unique=True,nullable=False)
    info_id = Column(Integer, ForeignKey('hw.id'))
    person_id = Column(Integer,unique=True,nullable=False)
    person_name = Column(String(30),unique=True,nullable=False)
    #user_id = Column(Integer, ForeignKey('user.id'))
    #user_name = Column(String, ForeignKey('user.username'))
    commented_post = relationship('DbHomework', back_populates='commentby')
    #commented_owner = relationship('DbUser', back_populates='comments')
