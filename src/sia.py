import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer


def sentimentAnalysis(sentence):
    sia = SentimentIntensityAnalyzer()
    polarity = sia.polarity_scores(sentence)
    pol = polarity['compound']
    return pol


def grade_to_sent(grade):
    if grade >= 0.05:
        return 'positive'
    elif grade <= -0.05:
        return 'negative'
    else:
        return 'neutral'

def main_sent(df,main_characters):
    char_sent = {}
    main_sentiment = {}

    for character in main_characters:
        char_sent[character] = dict(df[df['author']==character].sentiment.value_counts())

    for char in list(df.author.unique()):
        main_sentiment[char] = max(char_sent[char], key=char_sent[char].get) 
    return main_sentiment