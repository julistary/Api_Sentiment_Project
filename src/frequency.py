import pandas as pd
import src.downloading_and_cleaning as dc
import nltk
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
import collections
import regex
import requests

def clean_script(whole_script):
    whole_script = whole_script.replace("[", "")
    whole_script = whole_script.replace("\\x92", "")
    whole_script = whole_script.replace("\"","")
    whole_script = whole_script.replace("'","")
    whole_script = whole_script.replace(",","")
    whole_script = whole_script.replace(".","")
    whole_script = whole_script.replace("!","")
    whole_script = whole_script.replace("?","")
    whole_script = whole_script.replace(")","")
    whole_script = whole_script.replace("(","")
    return whole_script

def stopwds():
    stop_words = stopwords.words('english')
    stop_words += ['tell', 'im', 'hi','uh' ,'oh', 'dont', 'well', 'know', 'gonna', 'get', 'okay', 'youre', 'like', 'thats', 'yeah', 'think', 'she', 'yknow', 'really', 'mean', 'right', 'look', 'to', 'go', 'hey', 'uhh', 'got', 'come', 'see', 'cant', 'one', 'want', 'going', 'say', 'guys', 'good', 'back', 'god', 'ok', 'wanna']
    return stop_words


def commonwds(main_characters,df,stop_words):
    most_common = {}
    for character in main_characters:
        whole_script = str(list(df[df['author'] == character].quote))
        whole_script = clean_script(whole_script)
        wordcount = {}
        for word in whole_script.lower().split():
            if word not in stop_words:
                if word not in wordcount:
                    wordcount[word] = 1
                else:
                    wordcount[word] += 1
        word_counter = collections.Counter(wordcount)
        for word, count in word_counter.most_common(2):
            most_common[character] = word
    return most_common

def whole_script_common(df,main_characters,stop_words):
    whole = ""
    word_c = {}
    for character in main_characters:
        whole += str(list(df[df['author'] == character].quote))
        wordcount = {}
    whole = clean_script(whole)
    for word in whole.lower().split():
        if word not in stop_words:
            if word not in wordcount:
                wordcount[word] = 1
            else:
                wordcount[word] += 1
    word_counter = collections.Counter(wordcount)
    for word, count in word_counter.most_common(10):
        word_c[word] = count
    return (word_c)


def times(main_characters):
    import re
    url_times = "http://localhost:5000/times/"
    times = {}
    for c in main_characters:
        person = c
        nr_quotes = requests.get(url_times + person).content
        nr = re.findall(r'\d+',str((nr_quotes)))
        times[c] = int(nr[0])
    return times