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

#use for hw below
class DbUser(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(30), unique=True, nullable=False)
    email = Column(String(30), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    is_admin = Column(Boolean, default=False, nullable=True)
    created_products = relationship('DbProduct', back_populates='owner')
    
class DbHomework(Base):
    __tablename__ = 'hw'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(30), unique=True, nullable=False)
    username = Column(String(30), unique=True, nullable=False)
    content = Column(String(30), unique=True, nullable=False)
    contentlong = Column(String(30), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    #use for related below
    article_liked = relationship('DbLike', back_populates ='liked_article')
    article_commented = relationship('DbComment', back_populates ='commented_article')

class DbLike(Base):
    __tablename__ = 'like'
    id = Column(Integer, primary_key=True, index=True)
    article_id = Column(Integer, ForeignKey('hw.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    liked_article = relationship('DbArticle', back_populates='article_like')
    liked_user = relationship('DbUser', back_populates='press_like')

class DbComment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    article_id = Column(Integer, ForeignKey('hw.id'))
    user_id = Column(Integer, ForeignKey('user.id'))
    commented_article = relationship('DbHomework', back_populates='article_commented')
    
