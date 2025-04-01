import sqlite3

def create_database():
    with sqlite3.connect('my_database.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS MyTable (
            id INTEGER PRIMARY KEY,
            money REAL DEFAULT 110.00
        )
        ''')
        conn.commit()

def add_user_to_db(user_id):
    with sqlite3.connect('my_database.db') as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO MyTable (id, money) VALUES (?, ?)", (user_id, 110.00))
        conn.commit()

def user_exists(user_id):
    with sqlite3.connect('my_database.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM MyTable WHERE id = ?", (user_id,))
        return cursor.fetchone()[0] > 0

def get_user_balance(user_id):
    with sqlite3.connect('my_database.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT money FROM MyTable WHERE id = ?", (user_id,))
        result = cursor.fetchone()
        return result[0] if result else None

def update_user_balance(user_id, amount):
    with sqlite3.connect('my_database.db') as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE MyTable SET money = money + ? WHERE id = ?", (amount, user_id))
        conn.commit()

create_database()