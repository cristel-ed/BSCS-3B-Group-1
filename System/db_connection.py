import mysql.connector

# Establish the database connection
def get_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='evaluation system'
    )

def check_user_exists(username, student_id):
    """Check if the username or student ID already exists in the database."""
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = %s OR student_id = %s"
    cursor.execute(query, (username, student_id))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result is not None

def insert_user(first_name, last_name, student_id, course, year_section, username, password):
    """Insert a new user into the database."""
    # Check if the user already exists
    if check_user_exists(username, student_id):
        return False  # User exists, do not proceed

    conn = get_connection()
    cursor = conn.cursor()
    query = """
    INSERT INTO users (first_name, last_name, student_id, course, year_section, username, password)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (first_name, last_name, student_id, course, year_section, username, password))
    conn.commit()
    cursor.close()
    conn.close()
    return True

def verify_user(username, password):
    """Verify the user's credentials against the database."""
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result is not None


def verify_admin(username, password):
    """Verify the admin's credentials against the database."""
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM admins WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result is not None



