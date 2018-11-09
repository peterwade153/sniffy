import ssl

from bs4 import BeautifulSoup
import requests

import nltk
nltk.download('punkt')
nltk.download("stopwords")
from nltk.corpus import stopwords

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plot

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

from app.db_handler.db_helper import Text

#create an instance of the analyser
analyser = SentimentIntensityAnalyzer()


class Sniff():
    """
    Crawls a page to fetch text
    """

    def __init__(self, url):
        self.url = url

    def fetch_data(self):
        """
        Fetches data from a webpage and parse it then pick out the text. 
        """
        res =  requests.get(self.url, headers={'User-Agent': 'Mozilla/5.0'})
        if res.status_code == 200:
            html = res.text.strip()
            return html

    def format_data(self, html):
        """
        Formats the fetched data to actual text, removing the html tags.
        """
        soup = BeautifulSoup(html, "html5lib")
        try:
            text = soup.find("div", 'post-body entry-content')
            clean_text = text.get_text()
        except AttributeError:
            pass
        return clean_text

    def tokenize_words (self, clean_text):
        """
        Packs all words in sentences into a list
        """
        words = nltk.word_tokenize(clean_text)
        tokens = [w for w in words]
        return tokens

    def remove_stop_words(self, tokens):
        """
        Remove stop words from the text
        """
        cleaned_data = []
        for token in tokens:
            if token.lower() not in set(stopwords.words('english')):
                cleaned_data.append(token)
        return cleaned_data

    def word_frequency(self, cleaned_data):
        """
        This function picks cleaned text from the format_data() function
        Returns words frequency and also plot their frequency dist graph
        """
        new_data = [] 
        freq = nltk.FreqDist(cleaned_data)
        freq.plot(50, cumulative=False)
        for key, value in freq.items():
            new_data.append({key:value})
        return new_data

    def get_sentence_polarity(self, clean_text):
        """
        Performing sentiment analysis on text statements to get their polarity
        """
        sents = nltk.sent_tokenize(clean_text, language='english')
        all_sents = [sent for sent in sents]

        #analyse each of the sentences
        response = []
        for sent in all_sents:
            res = analyser.polarity_scores(sent)
            response.append({sent:res['compound']})
            res = Text(sent, res['compound'])
            res.save_text()
        return response