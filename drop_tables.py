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

def drop_table(table_name):
    """Drop a specified table from the database."""
    conn = create_connection()
    if conn is None:
        print("Failed to create the database connection.")
        return

    try:
        c = conn.cursor()
        c.execute(f"DROP TABLE IF EXISTS {table_name};")
        conn.commit()
        print(f"Table '{table_name}' dropped successfully.")
    except Error as e:
        print(f"Error dropping table '{table_name}':", e)
    finally:
        conn.close()

if __name__ == '__main__':
    # List the tables you want to drop
    tables_to_drop = ['AssignedForms']  # Add more table names as needed

    for table in tables_to_drop:
        drop_table(table)

create_connection()
