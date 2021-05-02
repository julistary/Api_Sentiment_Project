from config.configuration import db, collection

def number_quotes(character):
    """
    Function that returns the number of quotes that a certain character says.
    """
    proj = {"_id": 0, "index": 0}
    query = {"author": f"{character}"}
    nr = len(list(collection.find(query,proj)))
    return f"{character} says {nr} quotes"

def quotes_character(character):
    """
    Function that returns all the quotes that a certain character says.
    """
    proj = {"_id": 0, "index": 0}
    query = {"author": f"{character}"}
    quotes = list(collection.find(query,proj))
    return quotes

def quotes_episode(episode_title):
    """
    Function that returns all the quotes of a certain episode (name of the episode must be given).
    """
    proj = {"_id": 0, "index": 0}
    query = {"episode_title": f"{episode_title}"}
    quotes = list(collection.find(query,proj))
    return quotes

def quotes_season(season):
    """
    Function that returns all the quotes of a certain season.
    """
    proj = {"_id": 0, "index": 0}
    query = {"season": f"{season}"}
    quotes = list(collection.find(query,proj))
    return quotes


def quotes_season_episode(season, episode):
    """
    Function that returns all the quotes of a certain episode (number of the episode and must be given).

    """
    proj = {"_id": 0, "index": 0}
    query = {"season": f"{season}", "episode_number": f"{episode}"}
    quotes = list(collection.find(query,proj))
    return quotes

def quotes_season_episode_character(season, episode,character):
    """
    Function that returns all the quotes of a certain episode said by a certain character (number of the episode and must be given).
    """
    proj = {"_id": 0, "index": 0}
    query = {"season": f"{season}", "episode_number": f"{episode}", "author": f"{character}"}
    quotes = list(collection.find(query,proj))
    return quotes

def quotes_word(word):
    """
    Function that returns all the quotes that contains a certain word or sentence.

    """
    proj = {"_id": 0, "index": 0}
    query = {"quote" : {'$regex':f"{word}"}}
    quotes = list(collection.find(query,proj))
    return quotes

def sentiment(character):
    """
    Function that returns the main sentiment of a certain character.
    """
    proj = {"_id": 0, "word": 0}
    query = {"character" : f"{character}"}
    sent= list(collection.find(query,proj))
    return sent

def word(character):
    """
    Function that returns the most repeated word of a certain character

    """
    proj = {"_id": 0, "sentiment": 0}
    query = {"character" : f"{character}"}
    wrd= list(collection.find(query,proj))
    return wrd