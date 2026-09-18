from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker , Session
from sqlalchemy.ext.declarative import declarative_base
from typing import Annotated
from fastapi import Depends

SQLALCHEMY_DATABASE_URL_URI="postgresql://postgres:postgres@localhost:5432/DungeonsAndOragons"


# DEF ENGINE


engine=create_engine(SQLALCHEMY_DATABASE_URL_URI)



#DEF OF SESSION
SessionLocal= sessionmaker(autoflush=False , autocommit=False , bind=engine)



# DEF BASE AN OBJECT TO USER


Base= declarative_base()




#DEPENDENCY

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

#DEPENDANCY ANNOTATED

bd_dependency = Annotated[Session,Depends(get_db)]


