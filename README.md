# 🟡🔴🔵 API SENTIMENT PROJECT: FRIENDS API 🟡🔴🔵

<img width=600 src="http://cdn3.upsocl.com/wp-content/uploads/2016/09/Noticia-111249-friends-serie-20_anos-20_datos-1.gif">

## Goal 🏁
This is a python project that was sent to us at the Ironhack data analytics bootcamp. 

The objective of the project is to you create an API. This API will be able to receive information, store it, or serve it when needed. 

## Tools ⚙️
The tools to be used are Flask, NLP, functions, string operations, pandas, mongo queries, Mongo DB,  etc. 

## Libraries 👩🏼‍🏫
- [Pandas](https://pandas.pydata.org/docs/)
- [Requests](https://docs.python-requests.org/en/master/)
- [Os](https://docs.python.org/3/library/os.html)
- [Tqdm](https://tqdm.github.io/)
- [Nltk](https://www.nltk.org/)
- [Matplotlib](https://matplotlib.org/)
- [Collections](https://docs.python.org/3/library/collections.html)
- [PyMongo](https://pymongo.readthedocs.io/en/stable/)
- [Json](https://docs.python.org/3/library/json.html)
- [Dotenv](https://pypi.org/project/python-dotenv/)
- [Re](https://docs.python.org/3/library/re.html)


## My project 👩🏼‍💻
The first thing I did was importing and cleaning a `Friends quotes` dataset from [Kaggle](https://www.kaggle.com/ryanstonebraker/friends-transcript). 

Then, I enriched it with the `machine learning`tool `nltk`: analyse, per character, the polarity of their predominant sentiments and the most repeated words.

Once it was ready, using an endpoint, I added the data to `MongoDB` so I could start creating `get endpoints`. 

The endpoints created are: 
* "http://localhost:5000/times/**character_name**/" : it gives the number of quotes that a certain character says.
* "http://localhost:5000/character/**character_name**/" : it gives all the quotes said by a certain character.
* "http://localhost:5000/season/**season_number**/" : it gives all the quotes from a certain season.
* "http://localhost:5000/episode/**episode_name**/" : it gives all the quotes from a certain episode (name of the episode must be introduced).
* "http://localhost:5000/season/**season_number**/episode/**episode_number**/" : it gives all the quotes from a certain episode (number of the episode and of the season must be introduced).
* "http://localhost:5000/season/**season_number**/episode/**episode_number**/character/**character_name**/" : it gives all the quotes from a certain episode said by a concrete character (number of the episode and of the season must be introduced).
* "http://localhost:5000/words/**word**/": it gives all the words that contain a certain word or sentence. 
* "http://localhost:5000/sentiment/**character_name**/": it gives the predominant sentiment polarity of a certain character.
* "http://localhost:5000/word/**character_name**/": it gives the most repeated word of a certain character.

⚠ What is enclosed in ** is the endpoint that must be added by the user to access the specific information. 

## Content of the repository 👀

- Src folder with the functions defined and documented
- Jupyter Notebook with the main program
- Environment.yml and requirements.txt
- Mongo_api folder with all the documents required for the API creation:
    * congif folder with configuration
    * tools folder with the functions 
    * mongoapi.py where the API is created 
    * README.md file
- Procfile, runtime.txt and dump/friends folder (required for deploying with Heroku)
- friends_json and script json created during its execution
- Data folder with the csv from Kaggle

## TO DO
- Deploy it to heroku 