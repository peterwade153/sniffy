from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import ssl


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


    def format_data(self, data):
        """
        formats the fetched data to actual text, removing the html tags.
        """
        soup = BeautifulSoup(data, "html5lib")
        
        #extract text and remove whitespaces from bit of text
        sample_text = soup.find("div", 'post-body entry-content')
        return sample_text



