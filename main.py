from fastapi import FastAPI, Query
from pathlib import Path
from herores import HEROES

app= FastAPI()

@app.get('/')

async  def hearbeast():
    return "APP running"

@app.get('/HEROES')
async def get_all_heroes():
    return HEROES

#GET BY univers (AS QUERY PARAM)
@app.get('/HEROES/univers')

async  def get_all_heroes_univers(univer_type:str=Query()):
    resultat=[]
    for hero in HEROES:
        if univer_type.casefold() in hero.get("univers").casefold():
            resultat.append(hero)
    return resultat





#GET BY RANK (AS QUERY PARAM)
@app.get('/HEROES/rank')

async  def get_all_heroes_rank(hero_rank:int=Query()):
    resultat=[]
    for hero in HEROES:
        if hero.get("rank")>= hero_rank:
            resultat.append(hero)
    return resultat



#GET ONE HEAD BY ID (PATH PARAM)

@app.get("hero/id/{hero_id}")

async def get_on_hero_by_id(her_id:int=Path()):
    for hero in HEROES:
        if hero.get("id")==her_id:
            return hero


@app.get("hero/identite_secrete/{identite_secrete_id}")

async def get_on_hero_by_indentite(identite_secrete_id: str=Path()):
    for hero in HEROES:
        if identite_secrete_id.casefold() in hero.get("identity_secret").casefold():
            return hero