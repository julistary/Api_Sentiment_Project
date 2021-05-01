from config.configuration import collection


def insert_character(author,episode_number,episode_title, quote,season):
    dict_insert = {"author": author,
    "episode_number": episode_number,
    "episode_title": episode_title,
    "quote": quote,
    "season": season
    }
    collection.insert_one(dict_insert)
    
