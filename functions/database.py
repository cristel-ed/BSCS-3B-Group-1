import sqlite3
from sqlite3 import Error

def create_connection():
    """Establish a connection to the SQLite3 database."""
    try:
        conn = sqlite3.connect('evaluation_system.db')  # Connect to SQLite3 database
        return conn
    except Error as e:
        print(e)
        return None

def insert_professor(name):
    """Insert a new professor into the professors table."""
    conn = create_connection()
    try:
        c = conn.cursor()
        c.execute('''INSERT INTO professors (name) VALUES (?)''', (name,))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        print("Professor already exists!")
        return False
    except Error as e:
        print("Error inserting professor:", e)
        return False
    finally:
        conn.close()

def get_all_professors():
    """Retrieve all professors from the database."""
    conn = create_connection()
    try:
        c = conn.cursor()
        c.execute("SELECT name FROM professors")
        return [row[0] for row in c.fetchall()]
    except Error as e:
        print("Error retrieving professors:", e)
        return []
    finally:
        conn.close()

def setup_database():
    """Create database and tables if they do not exist."""
    conn = create_connection()
    if conn is None:
        print("Failed to create the database connection.")
        return

    try:
        c = conn.cursor()

        # Users Table
        c.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        first_name TEXT NOT NULL,
                        last_name TEXT NOT NULL,
                        student_id TEXT NOT NULL UNIQUE,
                        course TEXT NOT NULL,
                        year_section TEXT NOT NULL,
                        username TEXT NOT NULL UNIQUE,
                        password TEXT NOT NULL)''')

        # Admins Table
        c.execute('''CREATE TABLE IF NOT EXISTS admins (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT NOT NULL UNIQUE,
                        password TEXT NOT NULL)''')

        # EvaluationForms Table
        c.execute('''CREATE TABLE IF NOT EXISTS EvaluationForms (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        form_url TEXT NOT NULL UNIQUE,
                        form_name TEXT NOT NULL)''')  # Added form_name column

        # AssignedForms Table
        c.execute('''CREATE TABLE IF NOT EXISTS AssignedForms (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        student_id TEXT NOT NULL,
                        form_url TEXT NOT NULL,
                        professor_name TEXT NOT NULL,
                        due_date TEXT NOT NULL,
                        completed INTEGER NOT NULL DEFAULT 0,
                        pending INTEGER NOT NULL DEFAULT 1,
                        FOREIGN KEY (student_id) REFERENCES users (student_id) ON DELETE CASCADE)''')

        # Professors Table
        c.execute('''CREATE TABLE IF NOT EXISTS professors (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL UNIQUE)''')

        conn.commit()
        print("Database setup completed successfully.")
    except Error as e:
        print("Error setting up the database:", e)
    finally:
        conn.close()

