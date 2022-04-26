from fastapi import APIRouter
from fastapi_pagination import add_pagination
from config.database import SessionLocal
from schemas.comment import comment, CommentBase, EpisodeComment, CharacterComment, CommentUpdate
from crud.comment import create_comment_character_episode, create_comment_episode, create_comment_character, load_comments
from models.comment import Comment
from models.user import User
from typing import Optional
from models.enums import CommentStatus
from routes.user import get_user
app = APIRouter()
session=SessionLocal()

@app.post("/comment_character_in_epidoe/", response_model=comment)
def create_comment_character_in_episode(character_data:CommentBase):  
	character_data= create_comment_character_episode(session, character_data)
	return character_data

@app.post('/add_comment_episode')
def create_episode_comment(comment:EpisodeComment):
    comment_episode=create_comment_episode(session,comment)
    return comment_episode

@app.post('/add_comment_character')
def create_character_comment(comment:CharacterComment):
    comment_episode=create_comment_character(session,comment)
    return comment_episode

@app.get("/comment", response_model=comment)
async def get_comment(id:int):
    db_comment = session.query(Comment).get(id)
    return db_comment

@app.get("/comments/page")
async def get_comments(character_id: Optional[int] = None, episode_id: Optional[int] = None, type:Optional[str] = None, comment:Optional[str] = None, status:Optional[str] = None):
    params = locals().copy()
    query = session.query(Comment)
    for attr in [x for x in params if params[x] is not None]:query = query.filter(getattr(Comment, attr).like(params[attr])) 
    session.commit()
    return query.all()

@app.put("/comment")
async def update_comment(id: int, character_update: CommentUpdate)->Comment:
    comment_info = session.query(Comment).get(id)
    comment_info.comment = character_update.comment
    session.commit()
    session.refresh(comment_info)
    return comment_info

@app.delete("/comment")
def delete_comment_info(id: int):
    comment_info = session.query(Comment).get(id)
    session.delete(comment_info)
    session.commit()
    return {'message': 'The comment is deleted successfully'}

@app.get('/export_comments')
async def export_comments():
    load_comments(session)
    return {'message': 'Comments are exported into csv'}

# This endpoint is used by the moderator to update the status of the comment to accepted or rejected status
@app.put("/set_comment_status")
async def moderator_update_comment_status(commentId: int, userId:int, commentStatus:CommentStatus)->Comment:
    comment_info = session.query(Comment).get(commentId)
    user_info = session.query(User).get(userId)
    if (user_info.role=="Moderator"):
        comment_info.status = commentStatus
    session.commit()
    session.refresh(comment_info)
    return comment_info

# This endpoint is used by the admin to update the status of the comment as new in the case of an accepted comment or to delete it
#  in the case of a rejected status.
@app.put("/modif_comment_status")
async def admin_update_comment_status(commentId: int, userId:int)->Comment:
    comment_info = session.query(Comment).get(commentId)
    user_info = session.query(User).get(userId)
    if (user_info.role=="Admin"):
        if (comment_info.status=="Approved"):
            comment_info.status = "New"
            session.commit()
            session.refresh(comment_info)
            return comment_info
        elif (comment_info.status=="Rejected"): 
            return delete_comment_info(commentId)

        add_pagination(app)