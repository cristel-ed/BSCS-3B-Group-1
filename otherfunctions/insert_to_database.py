import sqlite3
from sqlite3 import Error

def create_connection():
    """Establish a connection to the SQLite3 database."""
    conn = None
    try:
        conn = sqlite3.connect('evaluation_system.db')  # Connect to SQLite3 database
        return conn
    except Error as e:
        print(e)
    return conn

def create_tables():
    """Create the required tables in the database."""
    conn = create_connection()
    if conn is None:
        print("Failed to create the database connection.")
        return

    try:
        c = conn.cursor()
        # Create users table
        c.execute('''CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            student_id TEXT NOT NULL,
            course TEXT NOT NULL,
            year_section TEXT NOT NULL,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )''')

        # Create admins table
        c.execute('''CREATE TABLE IF NOT EXISTS admins (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )''')

        # Create evaluation forms table
        c.execute('''CREATE TABLE IF NOT EXISTS EvaluationForms (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL
        )''')

        conn.commit()
        print("Tables created successfully.")
    except Error as e:
        print("Error creating tables:", e)
    finally:
        if conn:
            conn.close()

def insert_default_evaluation_form():
    """Insert default evaluation questions into the database."""
    questions = [
        "Does the professor clearly explain the course material?",
        "Does the professor provide adequate feedback on assignments?",
        "Does the professor create a positive learning environment?",
        "Does the professor encourage student participation?",
        "Does the professor provide sufficient office hours?"
        "Does the professor clearly explain the course material?",
        "Does the professor provide adequate feedback on assignments?",
        "Does the professor create a positive learning environment?",
        "Does the professor encourage student participation?",
        "Does the professor provide sufficient office hours?"
    ]

    conn = create_connection()
    if conn is None:
        print("Failed to create the database connection.")
        return

    try:
        c = conn.cursor()
        for question in questions:
            c.execute('INSERT INTO EvaluationForms (question) VALUES (?)', (question,))
        conn.commit()
        print("Default evaluation form has been added to the database.")
    except Error as e:
        print("Error inserting default evaluation form:", e)
    finally:
        if conn:
            conn.close()

def setup_database():
    """Set up the database by creating tables and inserting default evaluation forms."""
    create_tables()
    insert_default_evaluation_form()

if __name__ == "__main__":
    setup_database()
