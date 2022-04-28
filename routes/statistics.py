""" Statistics API's."""

from fastapi import APIRouter
import pandas as pd
from config.database import SessionLocal
from crud.stat_comments import count_comment_per_episode, count_letters_comments_per_episode

app = APIRouter()
session=SessionLocal()

@app.get('/export_comment_per_episode')
def get_comment_per_episode():
    """ export comment per episode API."""
    count_comment_per_episode()
    return {'message': 'Comment per episode are exported into csv'}

@app.get('/letter_comment_per_episode')
def count_letters_comments_episode():
    """ export mean of letter's length of comment per episode API."""
    count_letters_comments_per_episode()
    return {'message': "Mean of letter's length in comment is exported"}

@app.get('/export_comment_with_rejeted_status')
def number_comments_with_rejected_status_per_episode():
    """ export comments with rejeted status per episode API."""
    df_comment=pd.read_csv('csv_files/exported_comments.csv')
    df_comment=df_comment[df_comment['type'] == 'Episode']
    df_comment=df_comment[df_comment['status'] == 'Rejected']
    size=df_comment.groupby(['episode_id']).size()
    size.to_csv('csv_files/comment_with_rejected_status_per_episode.csv')
