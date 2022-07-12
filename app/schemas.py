from time import timezone
from pydantic import BaseModel,EmailStr
from datetime import datetime
from abc import ABC
from typing import Optional
from pyparsing import Optional
from pydantic.types import conint

#view/interface for creating/u[dating a post
class PostBase(BaseModel):
    title:str
    content:str
    published:bool=True #user doesnt have to provide this field and it will default to true
 

class PostCreate(PostBase):
    pass

class UserOut(BaseModel):
    id: int
    email:EmailStr
    created_at:datetime
    
    class Config: #this class used to convert sqlalchemy model into an orm pydantic dictonary
     orm_mode=True

class Post(PostBase):
    id:int
    created_at:datetime
    owner_id: int
    owner:UserOut

    class Config: #this class used to convert sqlalchemy model into an orm pydantic dictonary
        orm_mode=True

class PostOut(BaseModel):
    Post:Post
    votes:int

    class Config: #this class used to convert sqlalchemy model into an orm pydantic dictonary
        orm_mode=True




class UserCreate(BaseModel):
    email:EmailStr
    password:str



class UserLogin(BaseModel):
    email:EmailStr
    password:str

class Token(BaseModel):
    access_token:str
    token_type:str
class TokenData(BaseModel):
    id:str
    
class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)

