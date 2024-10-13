# forms_database.py
import sqlite3
from sqlite3 import Error
from .database import create_connection  # Import create_connection if it's in another file

def get_all_forms():
    """Retrieve all evaluation forms."""
    conn = create_connection()
    if conn is None:
        print("Error: Unable to connect to the database.")
        return []

    try:
        c = conn.cursor()
        c.execute("SELECT id, form_url, form_name FROM EvaluationForms")
        return c.fetchall()
    except Error as e:
        print("Error retrieving forms:", e)
        return []
    finally:
        conn.close()

def insert_form(form_url, form_name):
    """Insert a new form into the EvaluationForms table."""
    conn = create_connection()
    if conn is None:
        print("Error: Unable to connect to the database.")
        return False

    try:
        c = conn.cursor()
        c.execute('''INSERT INTO EvaluationForms (form_url, form_name) VALUES (?, ?)''', (form_url, form_name))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        print("Error: Form already exists!")
        return False
    except Error as e:
        print("Error inserting form:", e)
        return False
    finally:
        conn.close()

def assign_form_to_student(student_id, form_url, professor_name, due_date):
    """Assign a form to a student."""
    conn = create_connection()
    if conn is None:
        print("Error: Unable to connect to the database.")
        return False

    try:
        c = conn.cursor()
        c.execute('''INSERT INTO AssignedForms (student_id, form_url, professor_name, due_date)
                     VALUES (?, ?, ?, ?)''', (student_id, form_url, professor_name, due_date))
        conn.commit()
        return True
    except Error as e:
        print("Error assigning form:", e)
        return False
    finally:
        conn.close()


def assign_form_to_all_students(form_url, professor_name, due_date):
    """Assign a form to a single professor for all students who do not have it assigned yet."""
    conn = create_connection()  # Connect to the database
    if conn is None:
        print("Error: Unable to connect to the database.")
        return False

    try:
        c = conn.cursor()

        # Get all students from the users table
        c.execute("SELECT student_id FROM users")
        students = c.fetchall()  # Fetch all student IDs
        print(f"Total students found: {len(students)}")  # Debug print

        for student in students:
            student_id = student[0]

            # Check if the student already has this form assigned by the specific professor
            c.execute("SELECT * FROM AssignedForms WHERE student_id = ? AND form_url = ? AND professor_name = ?", (student_id, form_url, professor_name))
            if c.fetchone():  # If a record exists, skip to the next student
                print(f"Form '{form_url}' already assigned to student '{student_id}' by professor '{professor_name}', skipping...")  # Debug print
                continue

            # Debug statement to see what is being assigned
            print(f"Assigning form '{form_url}' to student '{student_id}' by professor '{professor_name}' with due date '{due_date}'")

            # If not, assign the form to this student
            c.execute("INSERT INTO AssignedForms (student_id, form_url, professor_name, due_date) VALUES (?, ?, ?, ?)",
                      (student_id, form_url, professor_name, due_date))

        conn.commit()
        print("Assignments committed successfully.")  # Debug print
        return True  # Return True if assignments were successful

    except Exception as e:
        print(f"Error assigning form to professor {professor_name}: {e}")  # Log the error for debugging
        return False  # Return False if there was an error
    finally:
        conn.close()


def get_assigned_forms(student_id):
    """Retrieve assigned forms for a specific student."""
    conn = create_connection()
    if conn is None:
        print("Error: Unable to connect to the database.")
        return []

    try:
        c = conn.cursor()
        c.execute('''SELECT form_url, professor_name, due_date FROM AssignedForms WHERE student_id = ?''', (student_id,))
        return c.fetchall()
    except Error as e:
        print("Error fetching assigned forms:", e)
        return []
    finally:
        conn.close()

def delete_professor(professor_name):
    """Delete a professor from the database."""
    conn = create_connection()
    if conn is None:
        print("Error: Unable to connect to the database.")
        return False

    try:
        c = conn.cursor()
        c.execute("DELETE FROM professors WHERE name = ?", (professor_name,))
        conn.commit()
        return c.rowcount > 0  # Return True if a professor was deleted
    except Error as e:
        print(f"Error deleting professor: {e}")
        return False
    finally:
        conn.close()
