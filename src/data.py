import requests
from pymongo import MongoClient

def adding_character(character,url):
    okay = 0
    for scene in character:
        new = requests.post(url, data=scene)
        if new.content == b'OK':
            okay += 1
    if okay == len(character):
        print("New content added to de DB!!")