from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
from crud.episode import add_description_episode
import requests
from config.database import SessionLocal
import os

session=SessionLocal()
driver = webdriver.Chrome(ChromeDriverManager().install())
# Initializing the series that the loop will populate
community_episodes = []
community_images=[]
save_path='thumbnailFiles'

# For every season in the series-- range depends on the show
for sn in range(1,7):
    # Request from the server the content of the web page by using get(), and store the server’s response in the variable response
    driver.get('https://www.imdb.com/title/tt2861424/episodes?season='+ str(sn))
    content = driver.page_source
    # Parse the content of the request with BeautifulSoup
    page_html = BeautifulSoup(content, 'html.parser')

    # Select all the episode containers from the season's page
    episode_containers = page_html.find_all('div', class_ = 'info')
    print('ep',episode_containers)
    # For each episode in each season
    for episodes in episode_containers:
            # Get the info of each episode on the page
            season = sn
            episode_number = episodes.meta['content']
            title = episodes.a['title']
            description = episodes.find('div', class_='item_description').text
            #thumbnail = episodes.find('div', class_='hover-over-image zero-z-index')
            # Compiling the episode info
            add_description_episode(session,title,description)
            episode_data = [episode_number,title,season, description]
            # Append the episode info to the complete dataset
            community_episodes.append(episode_data)
    episode_images = page_html.find_all('div', class_ = 'image')
    for episodes in episode_images:
            # Get the info of each episode on the page
            thumbnail = episodes.find('img', class_='zero-z-index')
            # Append the episode info to the complete dataset
            community_images.append([thumbnail])
            if thumbnail:
                completeName = os. path. join(save_path, thumbnail['src'][36:])
                response = requests.get(thumbnail['src'], stream=True)
                file1 = open(completeName, 'wb').write(response.content)

import pandas as pd 
community_episodes = pd.DataFrame(community_episodes, columns = ['episode_number','title','season', 'description'])
community_images=pd.DataFrame(community_images, columns = ['thumbnail'])
community_episodes.to_csv('csv_files/description.csv')
community_images.to_csv('csv_files/thumbnail.csv')
