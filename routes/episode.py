from fastapi import APIRouter
from config.database import SessionLocal
from typing import List
from models.characterWithEpisode import Episode
from schemas.episode import episode

app = APIRouter()
session=SessionLocal()

@app.get("/episodes", response_model=List[episode])
async def get_episodes(skip: int = 0, limit: int = 100):
    db_episodes = session.query(Episode).offset(skip).limit(limit).all()
    return db_episodes
