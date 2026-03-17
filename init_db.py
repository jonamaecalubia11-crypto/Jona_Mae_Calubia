import sqlite3
import os

def init_db():
    if not os.path.exists('students.db'):
        connection = sqlite3.connect('students.db')
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                grade INTEGER
            )
        ''')
        connection.commit()
        connection.close()
        print("Database created successfully!")
    else:
        print("Database already exists.")
