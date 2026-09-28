from fastapi import FastAPI
from pathlib import Path

from starlette import status
from database import bd_dependency , engine
from sqlalchemy import text
import model
from routers.heroes_router import router
from routers.auth_router import router_auth
from model import Heroes

app= FastAPI()

model.Base.metadata.create_all(bind=engine)

app.include_router(router)  
app.include_router(router_auth)