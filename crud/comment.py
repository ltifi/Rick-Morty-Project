""" Comment crud file."""
from sqlalchemy.orm import Session
import pandas as pd
from schemas.comment_schema import CommentBase, EpisodeComment,CharacterComment
from models.comment import Comment

def create_comment_character_episode(session: Session, comment_data: CommentBase):
    """ Create new row comment about characetr in episode."""
    db_character_episode=Comment(character_id=comment_data.character_id,
    episode_id=comment_data.episode_id,type="character_in_episode",
    comment=comment_data.comment,status="Review")
    session.add(db_character_episode)
    session.commit()
    session.refresh(db_character_episode)
    return db_character_episode


def create_comment_episode(session: Session, comment_data: EpisodeComment):
    """ Create new row comment about episode."""
    db_episode=Comment(episode_id=comment_data.episode_id,character_id=None,
    type="Episode",comment=comment_data.comment,status="Review")
    session.add(db_episode)
    session.commit()
    session.refresh(db_episode)
    return db_episode

def create_comment_character(session: Session, comment_data: CharacterComment):
    """ Create new row comment about characetr."""
    db_character=Comment(character_id=comment_data.character_id,episode_id=None,
    type="Character",comment=comment_data.comment,status="Review")
    session.add(db_character)
    session.commit()
    session.refresh(db_character)
    return db_character

def load_comments(session: Session):
    """ load comments."""
    comment=session.query(Comment.character_id,Comment.episode_id,
    Comment.type,Comment.comment,Comment.status).all()
    df_comment = pd.DataFrame(comment, columns=['character_id',
    'episode_id','type','comment','status'])
    df_comment.to_csv('csv_files/exported_comments.csv',index=True)
