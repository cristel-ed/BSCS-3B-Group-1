import sqlite3
from sqlite3 import Error

# Function to create a connection to the SQLite3 database
def create_connection():
    conn = None
    try:
        conn = sqlite3.connect('evaluation_system.db')  # Connect to the SQLite3 database
        return conn
    except Error as e:
        print(e)
    return conn

# Function to create tables if they don't exist
def create_tables():
    conn = create_connection()
    if conn is None:
        print("Failed to create the database connection.")
        return

    try:
        c = conn.cursor()
        # Create table for users if it doesn't exist
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

        # Create table for admins if it doesn't exist
        c.execute('''CREATE TABLE IF NOT EXISTS admins (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )''')

        conn.commit()
        print("Tables created successfully.")
    except Error as e:
        print("Error creating tables:", e)
    finally:
        if conn:
            conn.close()

# Function to insert a new user into the users table
def insert_user(first_name, last_name, student_id, course, year_section, username, password):
    conn = create_connection()
    if conn is None:
        print("Failed to create the database connection.")
        return False

    try:
        c = conn.cursor()
        # Insert user data into the users table
        c.execute('''INSERT INTO users (first_name, last_name, student_id, course, year_section, username, password)
                     VALUES (?, ?, ?, ?, ?, ?, ?)''',
                  (first_name, last_name, student_id, course, year_section, username, password))

        conn.commit()
        print("User registered successfully.")
        return True
    except sqlite3.IntegrityError:
        print("User already exists!")
        return False
    except Error as e:
        print("Error inserting user:", e)
        return False
    finally:
        if conn:
            conn.close()

# Function to verify user credentials for login
def verify_user(username, password):
    conn = create_connection()
    if conn is None:
        print("Failed to create the database connection.")
        return False

    try:
        c = conn.cursor()
        # Check if the username and password exist in the users table
        c.execute('''SELECT * FROM users WHERE username = ? AND password = ?''', (username, password))
        user = c.fetchone()
        return user is not None  # Return True if the user exists, otherwise False
    except Error as e:
        print(e)
        return False
    finally:
        if conn:
            conn.close()

# Function to verify admin credentials for admin login
def verify_admin(username, password):
    conn = create_connection()
    if conn is None:
        print("Failed to create the database connection.")
        return False

    try:
        c = conn.cursor()
        # Check if the username and password exist in the admins table
        c.execute('''SELECT * FROM admins WHERE username = ? AND password = ?''', (username, password))
        admin = c.fetchone()
        return admin is not None  # Return True if the admin exists, otherwise False
    except Error as e:
        print(e)
        return False
    finally:
        if conn:
            conn.close()

# Create the tables when this script is first run
if __name__ == '__main__':
    create_tables()
