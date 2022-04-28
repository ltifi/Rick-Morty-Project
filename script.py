import json
from models.character_with_episode import Episode, Character
from crud.character import create_character
from crud.episode import create_episode
from crud.character_episode import create_episode_character_relation
from schemas.character_episode_schema import EpisodeCharacterRelationCreate
from config.database import SessionLocal

session=SessionLocal()

with open('./json/rick_morty-episodes_v1.json',encoding="utf8") as json_data:
    data_dict = json.load(json_data)
data_episodes = json.dumps(data_dict)
data_dict_episodes = json.loads(data_episodes)
for temp_data in data_dict_episodes:
    ep=Episode(name=temp_data['name'],air_date=temp_data['air_date'],episode=temp_data['episode'])
    create_episode(session,ep)
with open('./json/rick_morty-characters_v1.json',encoding="utf8") as json_data:
    data_dict = json.load(json_data)
data_characters = json.dumps(data_dict)
data_dict_characters = json.loads(data_characters)
for temp_data in data_dict_characters:
    ch=Character(name=temp_data['name'],status=temp_data['status'],species=temp_data['species'],type=temp_data['type'],gender=temp_data['gender'])
    create_character(session,ch)
    for ep_id in temp_data['episode']:
        epChr=EpisodeCharacterRelationCreate(character_id=temp_data['id'],episode_id=ep_id)
        create_episode_character_relation(session,epChr)
