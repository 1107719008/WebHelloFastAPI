from pydantic import BaseModel, validator, EmailStr
from typing import List


class ProductRequestSchema(BaseModel):
    category: str
    name: str
    sku: str
    price: int
    image: str
    description: str
    description_long: str
    currency: str
    countInStock: int
    owner_id: int


class ProductResponseSchema(ProductRequestSchema):
    id: int
    

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    username: str
    email: EmailStr
    is_admin: bool


class UserRequestSchema(UserBase):
    password1: str
    password2: str

    @validator('password2')
    def passwords_match(cls, v, values, **kwargs):
        if 'password1' in values and v != values['password1']:
            raise ValueError('passwords do not match')
        return v

    @validator("password1")
    def password_must_have_6_digits(cls, v):
        if len(v) < 6:
            raise ValueError("Password must have at least 6 digits")
        return v

class UserResponseSchema(UserBase):
    id: int
    
    class Config:
        orm_mode = True

class InfoRequestSchema(BaseModel):
    title: str
    username :str
    content : str
    contentlong : str
    like_count: int
    comment_count: int
    

class InfoResponseSchema(InfoRequestSchema):
    id: int
    class Config:
        orm_mode = True


class UpdateInfoRequestSchema(BaseModel):
    title: str
    username :str
    content : str
    contentlong : str
    password : str
    #info_id : int

class UpdateInfoResponseSchema(UpdateInfoRequestSchema):
    id: int
    class Config:
        orm_mode = True

class UserResponseWithProductsSchema(UserBase):
    id: int
    #created_products: List[ProductResponseSchema] = []

    class Config:
        orm_mode = True

#posted_articles: List[InfoResponseSchema] = []
#liked_articles: List[LikeResponseSchema] = []
#comment_articles: List[CommentResponseSchema] = []


#like and comment functionality below----------------
class LikeRequestSchema(BaseModel):
    user_id: int
    user_name: str
    article_id : int
    

class LikeResponseSchema(LikeRequestSchema):
    id : int
    article_id: int
    user_id: int

    class Config:
        orm_mode = True

class LikeResponseWithInfoSchema(LikeRequestSchema):
    id: int
    info_id: int
    liked_post: InfoResponseSchema

    class Config:
        orm_mode = True
#class LikeResponseWithProductSchema(LikeRequestSchema):
#    id: int
#    article_id: int
 #   liked_article: List[InfoResponseSchema] = []
#
 #   class Config:
 #       orm_mode = True

class CommentRequestSchema(BaseModel):
    article_id: int
    owner_id: int
    owner_name: str
    content: str

class CommentResponseSchema(CommentRequestSchema):
    id: int
    info_id: int
    #clicked_comment: InfoResponseSchema

    class Config:
        orm_mode = True

class CommentResponseWithInfoSchema(CommentRequestSchema):
    id: int
    card_id: int
    commented_post: InfoResponseSchema

    class Config:
        orm_mode = True

class InfoResponseWithLikesCommentSchema(InfoRequestSchema):
    id: int
    likeby: List[LikeResponseSchema] = []
    commentby: List[CommentResponseSchema] = []

    class Config:
        orm_mode = True



class ProductResponseWithUserSchema(ProductRequestSchema):
    id: int
    owner_id: int
    owner: UserResponseSchema

    class Config:
        orm_mode = True


