""" Comment model."""

from sqlalchemy import Column, Integer, String, ForeignKey,Enum
from sqlalchemy.orm import relationship
from config.database import engine, Base
from models.enums import CommentType, StatusType

class Comment(Base):
    """ Create comment model."""
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True, autoincrement=True)
    character_id = Column(Integer,ForeignKey('characters.id'),index=False, nullable=True)
    episode_id = Column(Integer,ForeignKey('episodes.id'), index=False, nullable=True)
    type =  Column(Enum(CommentType))
    comment = Column(String(200), unique=False, index=False, nullable=True)
    character = relationship("Character")
    episode = relationship("Episode")
    status= Column(Enum(StatusType))
Base.metadata.create_all(engine)
