"""Script scrapping."""
import os
import pandas as pd
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from crud.episode import add_description_episode
from config.database import SessionLocal

session=SessionLocal()

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--window-size=1200x800")
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=chrome_options)
community_episodes = []
community_images=[]
SAVE_PATH='thumbnailFiles'

for sn in range(1,7):
    driver.get('https://www.imdb.com/title/tt2861424/episodes?season='+ str(sn))
    content = driver.page_source
    page_html = BeautifulSoup(content, 'html.parser')
    episode_containers = page_html.find_all('div', class_ = 'info')
    for episodes in episode_containers:
        season = sn
        episode_number = episodes.meta['content']
        title = episodes.a['title']
        description = episodes.find('div', class_='item_description').text
        add_description_episode(session,title,description)
        episode_data = [episode_number,title,season, description]
        community_episodes.append(episode_data)
    episode_images = page_html.find_all('div', class_ = 'image')
    for episodes in episode_images:
        thumbnail = episodes.find('img', class_='zero-z-index')
        community_images.append([thumbnail])
        if thumbnail:
            completeName = os. path. join(SAVE_PATH, thumbnail['src'][36:])
            response = requests.get(thumbnail['src'], stream=True)
            file1 = open(completeName, 'wb').write(response.content)
list_attr = ['episode_number','title','season', 'description']
community_episodes = pd.DataFrame(community_episodes, columns = list_attr)
community_images=pd.DataFrame(community_images, columns = ['thumbnail'])
community_episodes.to_csv('/RickeyMorty/csv_files/description.csv')
community_images.to_csv('/RickeyMorty/csv_files/thumbnail.csv')
