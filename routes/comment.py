""" Comments API's."""

from typing import Optional
from fastapi import APIRouter
from fastapi_pagination import add_pagination
from config.database import SessionLocal
from schemas.comment_schema import CommentSchemaType, CommentBase, EpisodeComment, CharacterComment, CommentUpdate
from crud.comment import create_comment_character_episode, create_comment_episode, create_comment_character, load_comments
from models.comment import Comment
from models.user import User
from models.enums import CommentStatus

app = APIRouter()
session=SessionLocal()

@app.post("/comment_character_in_epidoe/", response_model=CommentSchemaType)
def create_comment_character_in_episode(character_data:CommentBase):
    """ Create comment about character in episode API."""
    character_data= create_comment_character_episode(session, character_data)
    return character_data

@app.post('/add_comment_episode')
def create_episode_comment(comment:EpisodeComment):
    """ Create comment about episode API."""
    comment_episode=create_comment_episode(session,comment)
    return comment_episode

@app.post('/add_comment_character')
def create_character_comment(comment:CharacterComment):
    """ Create comment about characters API."""
    comment_episode=create_comment_character(session,comment)
    return comment_episode

@app.get("/comment", response_model=CommentSchemaType)
async def get_comment(comment_id:int):
    """ get specific comment API."""
    db_comment = session.query(Comment).get(comment_id)
    return db_comment

@app.get("/comments/page")
async def get_comments(character_id: Optional[int] = None,
episode_id: Optional[int] = None, type:Optional[str] = None,
 comment:Optional[str] = None, status:Optional[str] = None):
    """ get all comments with pagination API."""
    params = locals().copy()
    query = session.query(Comment)
    for attr in [x for x in params if params[x] is not None]:
        query = query.filter(getattr(Comment, attr).like(params[attr]))
    session.commit()
    return query.all()

@app.put("/comment")
async def update_comment(comment_id: int, character_update: CommentUpdate)->Comment:
    """ Modifiy comment API."""
    comment_info = session.query(Comment).get(comment_id)
    comment_info.comment = character_update.comment
    session.commit()
    session.refresh(comment_info)
    return comment_info

@app.delete("/comment")
def delete_comment_info(comment_id: int):
    """ Delete comment API."""
    comment_info = session.query(Comment).get(comment_id)
    session.delete(comment_info)
    session.commit()
    return {'message': 'The comment is deleted successfully'}

@app.get('/export_comments')
async def export_comments():
    """ Export comments API."""
    load_comments(session)
    return {'message': 'Comments are exported into csv'}

@app.put("/set_comment_status")
async def moderator_update_comment_status(comment_id: int,
user_id:int, comment_status:CommentStatus)->Comment:
    """ This api is used by the moderator to update the status
     of the comment to accepted or rejected status """
    comment_info = session.query(Comment).get(comment_id)
    user_info = session.query(User).get(user_id)
    if user_info.role=="Moderator":
        comment_info.status = comment_status
    session.commit()
    session.refresh(comment_info)
    return comment_info

@app.put("/modif_comment_status")
async def admin_update_comment_status(comment_id: int,
 user_id:int)->Comment:
    """ This API is used by the admin to update the status of the comment as new in the case
    of an accepted comment or to delete it in the case of a rejected status."""
    comment_info = session.query(Comment).get(comment_id)
    user_info = session.query(User).get(user_id)
    if user_info.role=="Admin":
        if comment_info.status=="Approved":
            comment_info.status = "New"
            session.commit()
            session.refresh(comment_info)
            return comment_info
        if comment_info.status=="Rejected":
            return delete_comment_info(comment_id)

        add_pagination(app)
