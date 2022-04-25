from sqlalchemy.orm import Session
from schemas.comment import CommentBase, EpisodeComment,CharacterComment
from models.comment import Comment
import pandas as pd

def create_comment_character_episode(db: Session, comment_data: CommentBase):
    db_Character_Episode=Comment(character_id=comment_data.character_id,episode_id=comment_data.episode_id,type=comment_data.type,comment=comment_data.comment,status=comment_data.status)
    db.add(db_Character_Episode)
    db.commit()
    db.refresh(db_Character_Episode)
    return db_Character_Episode


def create_comment_episode(db: Session, comment_data: EpisodeComment):
    db_Episode=Comment(episode_id=comment_data.episode_id,character_id=None,type=comment_data.type,comment=comment_data.comment,status=comment_data.status)
    db.add(db_Episode)
    db.commit()
    db.refresh(db_Episode)
    return db_Episode

def create_comment_character(db: Session, comment_data: CharacterComment):
    db_Character=Comment(character_id=comment_data.character_id,episode_id=None,type=comment_data.type,comment=comment_data.comment,status=comment_data.status)
    db.add(db_Character)
    db.commit()
    db.refresh(db_Character)
    return db_Character

def load_comments(db: Session):
    comment=db.query(Comment.character_id,Comment.episode_id,Comment.type,Comment.comment,Comment.status).all()
    df = pd.DataFrame(comment, columns=['character_id','episode_id','type','comment','status'])
    df.to_csv('csv_files/exported_comments.csv',index=True)

