from config.configuration import db, collection

def number_quotes(character):
    proj = {"_id": 0, "index": 0}
    query = {"author": f"{character}"}
    nr = len(list(collection.find(query,proj)))
    return f"{character} says {nr} quotes"

def quotes_character(character):
    """
    Función que devuelve todas las frases un personaje
    """
    proj = {"_id": 0, "index": 0}
    query = {"author": f"{character}"}
    quotes = list(collection.find(query,proj))
    return quotes

def quotes_episode(episode_title):
    """
    Función que devuelve todas las frases un personaje
    """
    proj = {"_id": 0, "index": 0}
    query = {"episode_title": f"{episode_title}"}
    quotes = list(collection.find(query,proj))
    return quotes

def quotes_season(season):
    """
    Función que devuelve todas las frases un personaje
    """
    proj = {"_id": 0, "index": 0}
    query = {"season": f"{season}"}
    quotes = list(collection.find(query,proj))
    return quotes


def quotes_season_episode(season, episode):
    """
    Función que devuelve todas las frases un personaje
    """
    proj = {"_id": 0, "index": 0}
    query = {"season": f"{season}", "episode_number": f"{episode}"}
    quotes = list(collection.find(query,proj))
    return quotes

def quotes_season_episode_character(season, episode,character):
    """
    Función que devuelve todas las frases un personaje
    """
    proj = {"_id": 0, "index": 0}
    query = {"season": f"{season}", "episode_number": f"{episode}", "author": f"{character}"}
    quotes = list(collection.find(query,proj))
    return quotes

def quotes_word(word):
    """
    Función que devuelve todas las frases un personaje
    """
    proj = {"_id": 0, "index": 0}
    query = {"quote" : {'$regex':f"{word}"}}
    quotes = list(collection.find(query,proj))
    return quotes

def sentiment(character):
    """
    Función que devuelve todas las frases un personaje
    """
    proj = {"_id": 0, "word": 0}
    query = {"character" : f"{character}"}
    sent= list(collection.find(query,proj))
    return sent

def word(character):
    """
    Función que devuelve todas las frases un personaje
    """
    proj = {"_id": 0, "sentiment": 0}
    query = {"character" : f"{character}"}
    wrd= list(collection.find(query,proj))
    return wrd