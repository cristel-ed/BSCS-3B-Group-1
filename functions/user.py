import sqlite3
from sqlite3 import Error
from .database import create_connection


def insert_user(first_name, last_name, student_id, course, year_section, username, password):
    """Insert a new user into the users table."""
    conn = create_connection()
    try:
        c = conn.cursor()
        c.execute('''INSERT INTO users (first_name, last_name, student_id, course, year_section, username, password)
                     VALUES (?, ?, ?, ?, ?, ?, ?)''',
                  (first_name, last_name, student_id, course, year_section, username, password))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        print("User already exists!")
        return False
    except Error as e:
        print("Error inserting user:", e)
        return False
    finally:
        conn.close()

def verify_user(username, password):
    """Verify user credentials and return student ID if successful."""
    conn = create_connection()
    try:
        c = conn.cursor()
        c.execute('''SELECT student_id FROM users WHERE username = ? AND password = ?''',
                  (username, password))
        result = c.fetchone()
        return result[0] if result else None
    except Error as e:
        print("Error verifying user:", e)
        return None
    finally:
        conn.close()

# Add other user-related functions here
