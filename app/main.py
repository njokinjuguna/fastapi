from cmath import e
from pydoc import ModuleScanner
from turtle import title
from typing import Optional
from urllib import response
from fastapi import Body, FastAPI,Request,Response,status,HTTPException,Depends
from sqlalchemy.orm import Session
from .import models,schemas,utils
from .database import engine,get_db
from passlib.context import CryptContext
from .routers import post,user,auth,vote
from .config import Settings
from fastapi.middleware.cors import CORSMiddleware


#the code that helps create the models that create the tables in our database
#models.Base.metadata.create_all(bind=engine)



app = FastAPI()
#origins=["https://www.google.com","https://youtube.com"]
origins=["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=[],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#model
my_posts =[{
    "title":"title of post 1",
    "content":"content of post a",
    "id":1
},
{   
    "title":"favorite foods",
    "content":"i like pizza",
    "id":2
}]

def find_post(id):
    for p in my_posts:
        if p["id"]==id:
            return p
def find_index_post(id):
    for i,p in enumerate(my_posts):
        if p['id']==id:
            return i



#api's

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "welcome to my api!!"}



