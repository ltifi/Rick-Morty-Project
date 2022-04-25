import pandas as pd
import numpy as np


def count_comment_per_episode():
    df=pd.read_csv('csv_files/exported_comments.csv')
    df=df[df['type'] == 'Episode']
    commentsEp=df.groupby(['episode_id']).size()
    commentsEp.to_csv('csv_files/comment_per_episode.csv')

def count_letters_comments_per_episode():
    df=pd.read_csv('csv_files/exported_comments.csv')
    df=df[df['type'] == 'Episode']
    df = (df.groupby('episode_id')['comment']
                            .apply(lambda x: np.mean(x.str.len()))
                            .reset_index(name='mean_len_text'))
    df.to_csv('csv_files/numberLetter_comment_per_episode.csv')

    
