""" Episodes API's."""

from typing import Optional
from fastapi import APIRouter
from config.database import SessionLocal
from models.character_with_episode import Episode

app = APIRouter()
session=SessionLocal()

@app.get("/episodes/page")
async def get_comments(name: Optional[str] = None,
air_date: Optional[str] = None, episode:Optional[str] = None,
descritption:Optional[str] = None):
    """ Get episodes with pagination API."""
    params = locals().copy()
    query = session.query(Episode)
    for attr in [x for x in params if params[x] is not None]:
        query = query.filter(getattr(Episode, attr).like(params[attr]))
    session.commit()
    return query.all()
