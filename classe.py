from typing import List , Optional
from  pydantic import BaseModel, Field , constr 

class Hero:
    id:int
    nik_name:str
    full_name:List[str]
    occupation:List[str]
    power:List[str]
    hobby:List[str]
    type:str
    rank: int
    def __init__(self,id,nik_name,full_name,occupation, power,hobby,type,rank):
        self.id=id
        self.nik_name=nik_name
        self.nik_name=nik_name
        self.full_name=full_name
        self.occupation=occupation
        self.power=power
        self.hobby=hobby
        self.type=type
        self.rank=rank
        

class HeroValidation(BaseModel):
        id: Optional [int] =Field(default=None, ge=0 , description="ID N'EST PAS OBLIGATOIR")
        nik_name:str=Field(min_length=3)
        full_name:str =Field(min_length=3)
        occupation:List[constr(min_length=3)]
        power:List[constr(min_length=3)]
        hobby:List[constr(min_length=3)]
        type:str=Field(min_length=3)
        rank: int = Field(ge=0, le=100)
        model_config={
             "json_schema_estra":{
                  "exemple": {     
                            "nik_name":"ljg",
                            "full_name":"Ignyrçis",
                            "occupation":["Pyromancer", "Gladiator", "Executioner"],
                            "power":["Pyrokinesis", "Fire immunity"],
                            "hobby":["Sword fighting", "Gambling", "Hunting"],
                            "type":"toyota",
                            "rank":20
                  }
             }
        }



























































