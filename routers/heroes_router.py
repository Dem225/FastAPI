from fastapi import  Query , Body,HTTPException , APIRouter
from pathlib import Path
from herores import HEROES
from datas import users , prodruits

from classe import HeroValidation , Hero
from starlette import status
from database import bd_dependency , engine
from sqlalchemy import text
import model



from model import Heroes

router= APIRouter()

model.Base.metadata.create_all(bind=engine)



@router.get('/')
async  def hearbeast(db:bd_dependency):
    try:
        db.execute(text("SELECT 1"))
        return {"message": "DATABSE OK "}
    except Exception as e :
        return {"erroe": str(e)}

    
@router.get('/HEROES', status_code=status.HTTP_200_OK)
async def get_all_heroes(db: bd_dependency):
    return db.query(Heroes).order_by(Heroes.id.asc()).all()

@router.get('/user')
def get_all_users():
    return users
@router.get('/produits')
def get_all_produit():
    return prodruits
 


#GET BY type (AS QUERY PARAM)
@router.get('/HEROES/type',status_code=status.HTTP_200_OK)
async  def get_all_heroes_type(hero_type:str=Query()):
    resultat=[]
    for hero in HEROES:
        if hero_type.casefold() in hero.type.casefold():
            resultat.append(hero)
    return resultat





#GET BY RANK (AS QUERY PARAM)
@router.get('/HEROES/rank', status_code=status.HTTP_200_OK)

async  def get_all_heroes_rank(hero_rank:int=Query(ge=0 , le=100)):
    resultat=[]
    for hero in HEROES:
        if hero.rank>= hero_rank:
            resultat.append(hero)
    return resultat



#GET ONE HEAD BY ID (PATH PARAM)

@router.get("/HEROES/id/{hero_id}",  status_code=status.HTTP_200_OK)

async def get_on_hero_by_id(her_id:int=Path(gt=0)):
    for hero in HEROES:
        if hero.id == her_id:
            return hero
    raise HTTPException(status_code=404 , detail="HERO cant't be foubd")

@router.get("/HEROES/nike/{nike}", status_code=status.HTTP_200_OK)

async def get_on_hero_by_indentite(nike: str=Path(gt=0)):
    for hero in HEROES:
        if nike.casefold() in hero.nik_name.casefold():
            return hero
    raise HTTPException(status_code=404 , detail="HERO cant't be foubd")
#POST/CREATE (BY/BODY)

@router.post("/HEROES/create" , status_code=status.HTTP_201_CREATED ,)
async def create_hero(db:bd_dependency , hero_body:HeroValidation=Body()):
        new_hero= Heroes(**hero_body.model_dump(exclude={"id"}))
        db.add(new_hero)
        db.commit()



#UPATE  WITH PUT (BY BODY)
@router.put("/HEROES/update", status_code=status.HTTP_204_NO_CONTENT )
async def update_hero(hero_body:HeroValidation=Body()):
    hero_change=False
    for i in range(len(HEROES)):
        if HEROES[i].id == hero_body.id:
            hero_change=True
            HEROES[i]=Hero(**hero_body.model_dump())
    if not hero_change:
        raise HTTPException(status_code=404, detail="HERO cant't be foubd")


        

#DELET WHITH DELTE (BY BODY)

@router.delete("/HEROES/delet/{hero_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_hero(hero_id:int=Path(gt=0)):
    hero_change=False
    for i in range(len(HEROES)):
        if HEROES[i].id == hero_id:
            hero_change=True
            HEROES.pop(i)
            break
    if not hero_change:
        raise HTTPException(status_code=404, detail="HERO cant't be foubd")





