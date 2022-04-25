from fastapi import APIRouter
from fastapi_pagination import add_pagination
from config.database import SessionLocal
from schemas.comment import comment, CommentBase, EpisodeComment, CharacterComment, CommentUpdate
from crud.comment import create_comment_character_in_episode, create_comment_episode, create_comment_character
from models.comment import Comment
from typing import Optional

app = APIRouter()
session=SessionLocal()

@app.post("/comment_character_in_epidoe/", response_model=comment)
def create_comment_character_in_episode(character_data:CommentBase):  
	character_data= create_comment_character_in_episode(session, character_data)
	return character_data

@app.post('/add_comment_episode')
def create_episode_comment(comment:EpisodeComment):
    comment_episode=create_comment_episode(session,comment)
    return comment_episode

@app.post('/add_comment_character')
def create_character_comment(comment:CharacterComment):
    comment_episode=create_comment_character(session,comment)
    return comment_episode

@app.get("/comment/{id}", response_model=comment)
async def get_comments(id:int):
    db_characters = session.query(Comment).get(id)
    return db_characters

@app.get("/comments/page")
async def get_comments(character_id: Optional[int] = None, episode_id: Optional[int] = None, type:Optional[str] = None, comment:Optional[str] = None, status:Optional[str] = None):
    params = locals().copy()
    query = session.query(Comment)
    for attr in [x for x in params if params[x] is not None]:query = query.filter(getattr(Comment, attr).like(params[attr])) 
    session.commit()
    return query.all()

@app.put("/comment/{id}")
async def update_comment(id: int, character_update: CommentUpdate)->Comment:
    character_info = session.query(Comment).get(id)
    character_info.comment = character_update.comment
    session.commit()
    session.refresh(character_info)
    return character_info

@app.delete("/comment/{id}")
def delete_comment_info(id: int):
    user_info = session.query(Comment).get(id)
    session.delete(user_info)
    session.commit()
    return {'message': 'The comment is deleted successfully'}

add_pagination(app)