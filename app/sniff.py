from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import ssl


url = 'http://honorsprogram.gwublogs.com/2017/11/08/honorsproblems-ive-messed-up-everything-oh-no/'

class Sniff():

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

        # soup = BeautifulSoup(raw_text)
        soup = BeautifulSoup(raw_text, "html5lib")
        
        #extract text and remove whitespaces from bit of text
        sample_text = soup.find("div", 'post-body entry-content')
        return sample_text

