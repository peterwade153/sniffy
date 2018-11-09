from app.sniff import Sniff
from app.db_handler.db_setup import Database_handler

if __name__ == '__main__':
    url3 = "http://encouragementforeverydaystruggles.blogspot.com/"
    sd = Sniff(url3)
    data = sd.fetch_data()
    ls = sd.format_data(data)
    # ls = sd.tokenize_words(ls)
    # ls = sd.remove_stop_words(ls)
    # ls = sd.word_frequency(ls)
    sd.get_sentence_polarity(ls)
    # db = Database_handler()
    # db.create_table()
