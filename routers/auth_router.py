from fastapi import APIRouter , Body
from classe import PlayserValidation

router_auth=APIRouter()


@router_auth.post("/auth/register")


async  def register_player(player_body:PlayserValidation = Body()):
    return player_body