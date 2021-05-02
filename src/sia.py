import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer


def sentimentAnalysis(sentence):
    """
    Analyses the sentiment polarity of a sentence.
    Args:
        sentence(str): the sentence to analyse
    Returns:
        The sentiment polarity (as a float) - it's like a grade
    """
    sia = SentimentIntensityAnalyzer()
    polarity = sia.polarity_scores(sentence)
    pol = polarity['compound']
    return pol


def grade_to_sent(grade):
    """
    Transforms the grades obtained to a sentiment
    Args:
        grade(float): the grade obtained from de sentiment analysis
    Returns:
        The sentiment as a string
    """
    if grade >= 0.05:
        return 'positive'
    elif grade <= -0.05:
        return 'negative'
    else:
        return 'neutral'

def main_sent(df,main_characters):
    """
    Evaluates the main sentiment of a character
    Args:
        df (df): the dataframe to work with
        main_characters(list): the list of characters to work with
    Returns:
        A dictionary with the main sentiment of each character
    """
    char_sent = {}
    main_sentiment = {}

    for character in main_characters:
        char_sent[character] = dict(df[df['author']==character].sentiment.value_counts())

    for char in list(df.author.unique()):
        main_sentiment[char] = max(char_sent[char], key=char_sent[char].get) 
    return main_sentiment