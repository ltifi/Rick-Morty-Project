from fastapi import APIRouter
from config.database import SessionLocal
from crud.statComments import count_comment_per_episode, count_letters_comments_per_episode
import pandas as pd

app = APIRouter()
session=SessionLocal()

@app.get('/export_comment_per_episode')
def get_comment_per_episode():
    count_comment_per_episode()
    return {'message': 'Comment per episode are exported into csv'}

@app.get('/letter_comment_per_episode')
def count_letters_comments_episode():
    count_letters_comments_per_episode()
    return {'message': "Mean of letter's length in comment is exported"}

@app.get('/export_comment_with_rejeted_status')
def number_comments_with_rejected_status_per_episode():
    df=pd.read_csv('csv_files/exported_comments.csv')
    df=df[df['type'] == 'Episode']
    df=df[df['status'] == 'Rejected']
    size=df.groupby(['episode_id']).size()
    size.to_csv('csv_files/comment_with_rejected_status_per_episode.csv')

