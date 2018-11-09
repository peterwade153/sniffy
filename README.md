# Sniffy
Sniffy is a script built with ```Python3.6``` to craw a webpage and fetch data, and uses ```NLTK``` to perform analysis such as Word frequency. Application also uses a postgres database
The Application uses VADER (Valence Aware Dictionary and sEntiment Reasoner) a lexicon and rule-based sentiment analysis tool that is specifically attuned to sentiments expressed in social media, and works well on texts from other domains to perform sentiment analysis on the text obtained from a crawled page

## Installation
Create a Virtual environment

Clone the app
```
git clone https://github.com/peterwade153/sniffy.git
```

### Install Dependencies
This will install dependencies from the Pipfile
```
pipenv install
```

### Setup database
Create a database. Pass the Database_name, User and Password to the ```Database handler``` in the ```db_handler``` directory. On the Terminal to create the table
```
from app.db_handler.db_setup import Database_handler
db = Database_handler()
db.create_table()
```

### Run the app
```
python run.py
```