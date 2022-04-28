""" Statistics crud file."""

import pandas as pd
import numpy as np


def count_comment_per_episode():
    """ create a csv file for counting the number of comments per episode."""
    df_count=pd.read_csv('/RickeyMorty/csv_files/exported_comments.csv')
    df_count=df_count[df_count['type'] == 'Episode']
    comments_ep=df_count.groupby(['episode_id']).size()
    comments_ep.to_csv('/RickeyMorty/csv_files/comment_per_episode.csv')

def count_letters_comments_per_episode():
    """ create a csv file for counting the mean of letter's length of comments per episode."""
    df_count=pd.read_csv('/RickeyMorty/csv_files/exported_comments.csv')
    df_count=df_count[df_count['type'] == 'Episode']
    df_count = (df_count.groupby('episode_id')['comment']
                            .apply(lambda x: np.mean(x.str.len()))
                            .reset_index(name='mean_len_text'))
    df_count.to_csv('/RickeyMorty/csv_files/numberLetter_comment_per_episode.csv')
