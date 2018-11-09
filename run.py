from app.sniff import Sniff
from app.db_handler.db_setup import Database_handler

if __name__ == '__main__':
    url = 'http://honorsprogram.gwublogs.com/2017/11/08/honorsproblems-ive-messed-up-everything-oh-no/'
    url2 = "https://www.wintellect.com/containerize-python-app-5-minutes/"
    url3 = "http://encouragementforeverydaystruggles.blogspot.com/"
    sd = Sniff(url3)
    data = sd.fetch_data()
    ls = sd.format_data(data)
    # ls = sd.tokenize_words(ls)
    # ls = sd.remove_stop_words(ls)
    # ls = sd.word_frequency(ls)
    # ls = sd.get_sentence_polarity(ls)
    db = Database_handler()
    db.create_table()
    
