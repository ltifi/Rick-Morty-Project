from sqlalchemy import Boolean, Column, Integer, String, ForeignKey, Table, Enum, Text
from sqlalchemy.orm import relationship

from config.database import engine, Base,SessionLocal
import uuid
import enum



class CommentType(str, enum.Enum):
    episode = "Episode"
    character = "Character"
    characterInEpisode="character_in_episode"

class RoleType(str, enum.Enum):
    admin = "Admin"
    user = "User"
    moderator="Moderator"

class StatusType(str, enum.Enum):
    new = "New"
    review = "Review"
    Rejected="Rejected"
    approved="Approved"