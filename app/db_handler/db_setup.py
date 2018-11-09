import psycopg2


class Database_handler:

    def __init__(self):
        """
        Connect to the database
        """
        try:
            self.conn = psycopg2.connect(
                database="sniffy", 
                user="postgres", 
                password="admin", 
                port="5432"
            )
            self.conn.autocommit = True
            self.cur = self.conn.cursor()
        except:
            raise("Database connection failed")
    
    def create_table(self):
        """
        Creates the table to store data
        """
        query = ("""
            CREATE TABLE IF NOT EXISTS analytics(
                ID SERIAL PRIMARY KEY NOT NULL,
                SENTENCE TEXT NOT NULL,
                SENTIMENT REAL NOT NULL);
            """)
        try:
            self.cur.execute(query)
            print("database created successfully")
        except psycopg2.Error as e:
            raise e


