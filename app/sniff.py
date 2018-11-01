from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import ssl

import nltk
nltk.download('punkt')
nltk.download("stopwords")
from nltk.corpus import stopwords

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plot


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
        context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
        req = Request(self.url, headers={'User-Agent': 'Mozilla/5.0'})
        response = urlopen(req, context=context)
        raw_text = response.read()
        return raw_text

    def format_data(self, raw_data):
        """
        Formats the fetched data to actual text, removing the html tags.
        """
        soup = BeautifulSoup(raw_data, "html5lib")
        
        sample_text = soup.find("div", 'post-body entry-content')
        text = sample_text.get_text()
        return text

    def tokenize_words (self, data):
        """
        Packs all words in sentences into a list
        """
        words = nltk.word_tokenize(data)
        tokens = [w for w in words]
        return tokens

    def remove_stop_words(self, data):
        """
        Remove stop words from the text
        """
        cleaned_data = []
        for token in data:
            if token.lower() not in set(stopwords.words('english')):
                cleaned_data.append(token)
        return cleaned_data

    def word_frequency(self, data):
        """
        Returns words frequency and also their frequency dist
        """
        new_data = [] 
        freq = nltk.FreqDist(data)
        freq.plot(50, cumulative=False)
        for key, value in freq.items():
            new_data.append({key:value})
        return new_data
