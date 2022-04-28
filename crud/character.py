""" Character crud file."""

from sqlalchemy.orm import Session
from schemas.character_schema import CharacterCreate
from models.character_with_episode import Character

def create_character(session: Session, chr_data: CharacterCreate):
    """ Create new characetr row."""
    db_character = Character(id=chr_data.id,name=chr_data.name, status=chr_data.status,
    species=chr_data.species,type=chr_data.type,gender=chr_data.gender)
    session.add(db_character)
    session.commit()
    session.refresh(db_character)
    return db_character
