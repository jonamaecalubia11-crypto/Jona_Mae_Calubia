
import sqlite3

def create_db():
    connection = sqlite3.connect('database.db')  # creates the file
    cursor = connection.cursor()

    # Example table: students
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

if __name__ == "__main__":
    create_db()