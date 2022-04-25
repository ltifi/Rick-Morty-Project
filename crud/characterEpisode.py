from schemas.characterEpisode import episodeCharacterRelationCreate
from models.characterWithEpisode import EpisodeCharacterRelation
from sqlalchemy.orm import Session

def create_episodeCharacterRelation(db: Session,epChr_data: episodeCharacterRelationCreate):
    statement = EpisodeCharacterRelation.insert().values(character_id=epChr_data.character_id, episode_id=epChr_data.episode_id)
    db.execute(statement)
    db.commit()
    return epChr_data


