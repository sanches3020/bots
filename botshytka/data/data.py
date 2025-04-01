import sqlite3

def create_database():
    with sqlite3.connect('my_database.db') as conn:
        cursor = conn.cursor()
      
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS MyTable (
            id INTEGER PRIMARY KEY,
            fio TEXT,
            numbers TEXT,
            email TEXT,
            age INTEGER
        )
        ''')

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS start_reg (
            status BOOLEAN NOT NULL
        )
        ''')

        conn.commit()

create_database()