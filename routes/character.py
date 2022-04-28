""" Characters API's."""

from typing import Optional
from fastapi import APIRouter
from fastapi_pagination import add_pagination
from models.character_with_episode import Character
from config.database import SessionLocal

app = APIRouter()
session=SessionLocal()

@app.get("/characters/page")
async def get_characters(name: Optional[str] = None,status: Optional[str] = None,
species:Optional[str] = None, type:Optional[str] = None, gender:Optional[str] = None):
    """ Get characters API."""
    params = locals().copy()
    query = session.query(Character)
    for attr in [x for x in params if params[x] is not None]:
        query = query.filter(getattr(Character, attr).like(params[attr]))
    session.commit()
    return query.all()
add_pagination(app)
