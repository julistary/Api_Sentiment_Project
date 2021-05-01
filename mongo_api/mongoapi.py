from flask import Flask, request
from flask import jsonify
import json
import markdown.extensions.fenced_code
import tools.getdata as get
import tools.postdata as pos



app = Flask(__name__)


@app.route("/")
def index():
    readme_file = open("Readme.md", "r")
    md_template = markdown.markdown( 
        readme_file.read(), extensions=["fenced_code"]
    )
    return md_template

@app.route("/times/<name>")
def nr_of_quotes(name):
    nr = get.number_quotes(name)
    return nr

@app.route("/character/<name>")
def quotesbycharacter(name):
    quotes = get.quotes_character(name)
    return jsonify(quotes)

@app.route("/episode/<title>")
def quotesbyepisode(title):
    quotes = get.quotes_episode(title)
    return jsonify(quotes)

@app.route("/season/<s>")
def quotesbyseason(s):
    quotes = get.quotes_season(s)
    return jsonify(quotes)

@app.route("/season/<s>/episode/<e>")
def quotesbyseasonepisode(s,e):
    quotes = get.quotes_season_episode(s,e)
    return jsonify(quotes)

@app.route("/season/<s>/episode/<e>/character/<name>")
def quotesbyseasonepisodecharacter(s,e,name):
    quotes = get.quotes_season_episode_character(s,e,name)
    return jsonify(quotes)

@app.route("/words/<w>")
def quotesbyword(w):
    quotes = get.quotes_word(w)
    return jsonify(quotes)


@app.route("/newcharacter", methods=["POST"])
def insertcharacter():
    author = request.form.get("author")
    episode_number = request.form.get("episode_number")
    episode_title = request.form.get("episode_title")
    quote = request.form.get("quote")
    season = request.form.get("season")
    pos.insert_character(author, episode_number, episode_title, quote, season)
    return "OK"


@app.route("/sentiment/<character>")
def sentimentch(character):
    sentiment_ = get.sentiment(character)
    return jsonify(sentiment_)

@app.route("/word/<character>")
def wordch(character):
    sentiment_ = get.word(character)
    return jsonify(sentiment_)


app.run("0.0.0.0", 5000, debug=True)