from requests import Session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sqlalchemy as sa 
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .config import Settings



SQLALCHEMY_DATABASE_URL=f'{Settings.database_client}://{Settings.database_username}:{Settings.database_password}@{Settings.database_hostname}/{Settings.database_name}'
# #the engine used to establish the connection bwtn the sqlalchemy and your database
engine=create_engine(SQLALCHEMY_DATABASE_URL)
#engine=connection_url
# #create a session for the connection
SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base=declarative_base()

#this function is called a dependancy and is related to the db connection;in that when a connection is esbalished then a session is started till when the connectio
#is close...hence this file is linked to line 12(from .database import engine,SessionLocal)
#db connection
while True:
    try:
        def get_db():
            db=SessionLocal()
            try:
                yield db
            finally:
                db.close()

        print("Database connection was succesfull!!!!!")
        break;
    except Exception as error:
        print("connecting to database failed")
        print("Error: ",error)
        time.sleep(2)



