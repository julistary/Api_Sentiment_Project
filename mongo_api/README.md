
# API Documentation 📄

* "http://localhost:5000/times/**character_name**/" : it gives the number of quotes that a certain character says.
* "http://localhost:5000/character/**character_name**/" : it gives all the quotes said by a certain character.
* "http://localhost:5000/season/**season_number**" : it gives all the quotes from a certain season.
* "http://localhost:5000/episode/**episode_name**" : it gives all the quotes from a certain episode (name of the episode must be introduced).
* "http://localhost:5000/season/**season_number**/episode/**episode_number**" : it gives all the quotes from a certain episode (number of the episode and of the season must be introduced).
* "http://localhost:5000/season/**season_number**/episode/**episode_number**/character/**character_name**" : it gives all the quotes from a certain episode said by a concrete character (number of the episode and of the season must be introduced).
* "http://localhost:5000/words/**word**": it gives all the words that contain a certain word or sentence. 
* "http://localhost:5000/sentiment/**character_name**": it gives the predominant sentiment polarity of a certain character.
* "http://localhost:5000/word/**character_name**": it gives the most repeated word of a certain character.

⚠ What is enclosed in asterisks is the endpoint that must be added by the user to access the specific information. 

## Some examples: 

#### ¿How many quotes does Monica say?

url = "http://localhost:5000/times/" 
person = "Monica" 
times = requests.get(url + person) 
times.content  

<img width=300 src="https://media.giphy.com/media/LaabpwEUXVUhq/giphy.gif">

#### Give me a quote from Rachel

url = "http://localhost:5000/character/"
person = "Rachel"
quotes = requests.get(url + person).json()
quotes[18076]['quote']

<img width=300 src="https://media.giphy.com/media/igsmXEkeyfPPgfU2yI/giphy.gif">

#### Give me a quote from the season 5

url = "http://localhost:5000/season/"
person = "5"
quotes = requests.get(url + person).json()
f"{quotes[9580]['author']} - {quotes[9580]['quote']}"

<img width=300 src="https://media.giphy.com/media/llToceLTKQj0R1Asid/giphy.gif">

#### Give me a quote from the episode ` Ross's Tan `

url_times = "http://localhost:5000/episode/"
person = "Ross's Tan"
quotes = requests.get(url_times + person).json()
quotes[88]['quote']

<img width=300 src="https://media.giphy.com/media/12bO6mIZRgRHKU/giphy.gif">

#### Give me a quote from the `S10 E13 `

url_1 = "http://localhost:5000/season/"
url_2 = "/episode/"
season = "10"
episode = "13"
quotes = requests.get(url_1 + season + url_2 + episode).json()
quotes[9]['quote']

<img width=300 src="https://media.giphy.com/media/XdU9ThNglPBHLsOjDz/giphy.gif">

#### Give me a quote from Janice from the `S5 E12 `

url_1 = "http://localhost:5000/season/"
url_2 = "/episode/"
url_3 = "/character/"
season = "5"
episode = "12"
character = "Janice"
quotes = requests.get(url_1 + season + url_2 + episode + url_3 + character).json()
quotes[3]['quote']

<img width=300 src="https://media.giphy.com/media/hXOc9DJufLxpzo82zq/giphy.gif">

#### Give me a quote that contains `Pivot`

url = "http://localhost:5000/words/"
word = "Pivot"
quotes = requests.get(url + word).json()
quotes[0]['quote']

<img width=300 src="https://media.giphy.com/media/2OP9jbHFlFPW/giphy.gif">

#### How would you define Phoebe?

url = "http://localhost:5000/sentiment/"
character = "Phoebe"
sent = requests.get(url + character).json()
sent[0]['sentiment']

<img width=300 src="https://media.giphy.com/media/LPs5pRt1OiaHqgTQoT/giphy.gif">

#### What is the word Rachel says most often?

url = "http://localhost:5000/word/"
character = "Chandler"
sent = requests.get(url + character).json()
sent[0]['word']

<img width=300 src="https://media.giphy.com/media/KCkFCX7iyRvsmq3rRZ/giphy.gif">