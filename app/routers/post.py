from fastapi import Body, FastAPI,Request,Response,status,HTTPException,Depends,APIRouter
from pyparsing import Optional
from sqlalchemy.orm import Session
from typing import List,Optional
from ..import models,schemas,utils,oauth2
from ..database import get_db
from sqlalchemy import func

router=APIRouter(
    prefix="/posts",
    tags=['Posts']
)




#****getting all post/records
@router.get("/",response_model=List[schemas.PostOut])
def get_posts(db:Session=Depends(get_db),current_user: int= Depends(oauth2.get_current_user),
limit: int =10,skip: int =0,search: Optional[str]=""):
       
       print(search)
       
       #posts=db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
      
       posts=db.query(models.Post,func.count(models.Vote.post_id).label("votes")).join(models.Vote,models.Vote.post_id == models.Post.id,isouter=True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
       

       return posts

#****creating/adding a post/record
#****the hhtp status code 201 is used/applied when you are creating a new post so instead
# of having status code 200  
@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.Post)
def create_posts(post:schemas.PostCreate,db:Session=Depends(get_db),current_user: int= Depends(oauth2.get_current_user)):
    # cursor.execute("""INSERT INTO posts (title,content,published)
    # VALUES (%s,%s,%s)RETURNING *
    #  """,(post.title,post.content,post.published))

    # new_post=cursor.fetchone()
    # conn.commit()

    # # post_dict=post.dict()
    # # post_dict['id']=randrange(0,1000000)
    # # my_posts.append(post_dict)
   #new_post=models.Post(title=post.title,content=post.content,published=post.published)
   print(current_user.id)
   new_post=models.Post(owner_id=current_user.id,**post.dict()) #Hutu tustars tunamean unpacking a dictonary
   db.add(new_post)
   db.commit()
   db.refresh(new_post) #similar to the returning word in the sql statement
   return new_post

#title str,content str
#****getting the latest post/record
@router.get("/latest",response_model=schemas.Post)
def get_latest_post():
    post=my_posts[len(my_posts)-1]
    return post  

#*****getting individual post/record
@router.get("/{id}",response_model=schemas.PostOut)
def get_post(id:int,db:Session=Depends(get_db),current_user: int= Depends(oauth2.get_current_user)):         #[id:int]it makes sure the id variable passed is automatically converted into an int
    # cursor.execute("""SELECT * FROM  posts WHERE id =%s""",(str(id),))
    # post=cursor.fetchone()
    # print(post)
    print(current_user)
    #post_query= db.query(models.Post).filter(models.Post.id==id)
    postt=db.query(models.Post,func.count(models.Vote.post_id).label("votes")).join(models.Vote,models.Vote.post_id == models.Post.id,isouter=True).group_by(models.Post.id).filter(models.Post.id==id).first()
    print(postt)

   
    if not postt:
        raise HTTPException (status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id: {id} was not found")

    # if postt.owner_id != current_user.id:
    #     raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Not authorized to perform requested action")

    return postt
 
 #****deleting post
@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int,db:Session=Depends(get_db),current_user: int= Depends(oauth2.get_current_user)):
    # cursor.execute("""DELETE FROM posts WHERE id = %s returning* """,(str(id),))
    # deleted_post=cursor.fetchone()
    # conn.commit()
    print(current_user)
    post_query=db.query(models.Post).filter(models.Post.id==id)
    post=post_query.first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id: {id} does not exist")

    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Not authorized to perform requested action")



    post_query.delete(synchronize_session=False) 
    db.commit()   
    return Response(status_code=status.HTTP_204_NO_CONTENT)

#**** update post
@router.put("/{id}",response_model=schemas.Post)
def update_post(id: int,updated_post:schemas.PostCreate, db:Session=Depends(get_db),current_user: int= Depends(oauth2.get_current_user)):
    # cursor.execute("""UPDATE posts SET title = %s,content=%s,published=%s WHERE id=%s RETURNING *""",(post.title,post.content,post.published,str(id)))
    # updated_post=cursor.fetchone()
    # conn.commit()
    print(current_user)
    post_query=db.query(models.Post).filter(models.Post.id==id)
    post=post_query.first()

    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id: {id} does not exist")

    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Not authorized to perform requested action")

    post_query.update(updated_post.dict(),synchronize_session=False)
    db.commit()
    return post_query.first()
