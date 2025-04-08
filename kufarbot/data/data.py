import sqlite3

def create_database():
    with sqlite3.connect('my_database.db') as conn:
        cursor = conn.cursor()
      
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS MyTable (
            id INTEGER PRIMARY KEY,
            url TEXT,
            numbers TEXT,
            id_task TEXT
        )
        ''')

        conn.commit()

create_database()