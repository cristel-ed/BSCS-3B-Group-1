import sqlite3
from sqlite3 import Error
from .database import create_connection


def verify_admin(username, password):
    """Verify admin credentials for login."""
    conn = create_connection()
    try:
        c = conn.cursor()
        c.execute('''SELECT * FROM admins WHERE username = ? AND password = ?''',
                  (username, password))
        return c.fetchone() is not None
    except Error as e:
        print(e)
        return False
    finally:
        conn.close()

def insert_form(form_url, form_name):
    """Insert a new form into the EvaluationForms table."""
    conn = create_connection()
    try:
        c = conn.cursor()
        c.execute('''INSERT INTO EvaluationForms (form_url, form_name) VALUES (?, ?)''', (form_url, form_name))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        print("Form already exists!")
        return False
    except Error as e:
        print("Error inserting form:", e)
        return False
    finally:
        conn.close()

# Add other admin-related functions here
