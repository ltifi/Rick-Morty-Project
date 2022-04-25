from sqlalchemy.orm import Session
from schemas.character import CharacterCreate
from models.characterWithEpisode import Character

def create_character(db: Session, Chr_data: CharacterCreate):
    db_Character = Character(id=Chr_data.id,name=Chr_data.name, status=Chr_data.status,species=Chr_data.species,type=Chr_data.type,gender=Chr_data.gender)
    db.add(db_Character)
    db.commit()
    db.refresh(db_Character)
    return db_Character