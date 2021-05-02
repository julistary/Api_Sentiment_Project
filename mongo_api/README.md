
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

url = "http://localhost:5000/times/Monica" 

<img width=300 src="https://media.giphy.com/media/LaabpwEUXVUhq/giphy.gif">

#### Give me a quote from Rachel

url = "http://localhost:5000/character/Rachel"

<img width=300 src="https://media.giphy.com/media/igsmXEkeyfPPgfU2yI/giphy.gif">

#### Give me a quote from the season 5

url = "http://localhost:5000/season/5"


<img width=300 src="https://media.giphy.com/media/llToceLTKQj0R1Asid/giphy.gif">

#### Give me a quote from the episode ` Ross's Tan `

url = "http://localhost:5000/episode/Ross's Tan"

<img width=300 src="https://media.giphy.com/media/12bO6mIZRgRHKU/giphy.gif">

#### Give me a quote from the `S10 E13 `

url = "http://localhost:5000/season/10/episode/13"

<img width=300 src="https://media.giphy.com/media/XdU9ThNglPBHLsOjDz/giphy.gif">

#### Give me a quote from Janice from the `S5 E12 `

url= "http://localhost:5000/season/5/episode/12/Janice"

<img width=300 src="https://media.giphy.com/media/hXOc9DJufLxpzo82zq/giphy.gif">

#### Give me a quote that contains `Pivot`

url = "http://localhost:5000/words/Pivot"

<img width=300 src="https://media.giphy.com/media/2OP9jbHFlFPW/giphy.gif">

#### How would you define Phoebe?

url = "http://localhost:5000/sentiment/Phoebe"

<img width=300 src="https://media.giphy.com/media/LPs5pRt1OiaHqgTQoT/giphy.gif">

#### What is the word Chandler says most often?

url = "http://localhost:5000/word/Chandler"

<img width=300 src="https://media.giphy.com/media/H6hurOxfrUNWoChAVf/giphy.gif">