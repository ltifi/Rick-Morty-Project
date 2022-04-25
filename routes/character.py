from fastapi import APIRouter
from config.database import SessionLocal
from typing import List
from models.characterWithEpisode import Character
from schemas.character import character

app = APIRouter()
session=SessionLocal()

@app.get("/characters", response_model=List[character])
async def get_characters(skip: int = 0, limit: int = 100):
    db_characters = session.query(Character).offset(skip).limit(limit).all()
    return db_characters
