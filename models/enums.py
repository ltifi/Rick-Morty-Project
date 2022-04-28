""" Enumerations. """

import enum

class CommentType(str, enum.Enum):
    """ Comment type enumeration. """
    EPISODE = "Episode"
    CHARACTER = "Character"
    CHARACTERINEPISODE="character_in_episode"

class RoleType(str, enum.Enum):
    """ Role type enumeration. """
    ADMIN = "Admin"
    USER = "User"
    MODERATOR="Moderator"

class StatusType(str, enum.Enum):
    """ Comment type enumeration. """
    NEW = "New"
    REVIEW = "Review"
    REJECTED="Rejected"
    APPROVED="Approved"

class CommentStatus(str, enum.Enum):
    """ limited Comment type enumeration. """
    REJECTED="Rejected"
    APPROVED="Approved"
