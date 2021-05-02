import requests
from pymongo import MongoClient

def adding_character(character,url):
    """
    Calls the Friends API and add data to MongoDB.
    Args:
        character(str): the name of the character to work with
        url (str): the url with the endpoint required
    """
    okay = 0
    for scene in character:
        new = requests.post(url, data=scene)
        if new.content == b'OK':
            okay += 1
    if okay == len(character):
        print("New content added to de DB!!")