from db_setup import Database_handler

#create insatnce of the Database_handler
db = Database_handler()

class Text:
    """
    This will help in the saving of text
    """

    def __init__(self, text, sentiment):
        """
        Initialize text and it's sentiment
        """
        self.text = text
        self.sentiment = sentiment

    def save_text(self):
        """
        Saves text and corresponding sentiment to the database
        """
        add_text_query = ("""
        INSERT INTO analytics (SENTENCE,SENTIMENT) VALUES (%s, %s);
        """)
        db.cur.execute(add_text_query)
