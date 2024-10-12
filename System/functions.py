import sqlite3
from sqlite3 import Error
from tkinter import messagebox
import registerform
import loginform
import adminloginform
import studentdash
import admindash

# ------------------ Database Functions ------------------

# Create a connection to the SQLite3 database
def create_connection():
    """Establish a connection to the SQLite3 database."""
    conn = None
    try:
        conn = sqlite3.connect('evaluation_system.db')  # Connect to SQLite3 database
        return conn
    except Error as e:
        print(e)
    return conn

# Create tables if they don't exist
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

        conn.commit()
        print("Tables created successfully.")
    except Error as e:
        print("Error creating tables:", e)
    finally:
        if conn:
            conn.close()

# ------------------ User Functions ------------------

# Insert a new user into the users table
def insert_user(first_name, last_name, student_id, course, year_section, username, password):
    """Insert a new user into the users table."""
    conn = create_connection()
    if conn is None:
        print("Failed to create the database connection.")
        return False

    try:
        c = conn.cursor()
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

# Verify user credentials for login
def verify_user(username, password):
    """Verify user credentials for login."""
    conn = create_connection()
    if conn is None:
        print("Failed to create the database connection.")
        return False

    try:
        c = conn.cursor()
        c.execute('''SELECT * FROM users WHERE username = ? AND password = ?''', (username, password))
        user = c.fetchone()
        return user is not None
    except Error as e:
        print(e)
        return False
    finally:
        if conn:
            conn.close()

# Verify admin credentials for admin login
def verify_admin(username, password):
    """Verify admin credentials for login."""
    conn = create_connection()
    if conn is None:
        print("Failed to create the database connection.")
        return False

    try:
        c = conn.cursor()
        c.execute('''SELECT * FROM admins WHERE username = ? AND password = ?''', (username, password))
        admin = c.fetchone()
        return admin is not None
    except Error as e:
        print(e)
        return False
    finally:
        if conn:
            conn.close()

# ------------------ Password Visibility Functions ------------------

# Toggle show password
def view_pass(pass_entry, eye_button, hide_pass):
    """Toggle to show the password."""
    hide_pass.config(file='Image/view.png')
    pass_entry.config(show='')
    eye_button.config(command=lambda: hide_pass_func(pass_entry, eye_button, hide_pass))

# Toggle hide password
def hide_pass_func(pass_entry, eye_button, hide_pass):
    """Toggle to hide the password."""
    hide_pass.config(file='Image/hide.png')
    pass_entry.config(show='*')
    eye_button.config(command=lambda: view_pass(pass_entry, eye_button, hide_pass))

# ------------------ Registration and Login Functions ------------------

# Handle user registration
def register_user(
    fNameEntry, lNameEntry, studentIDEntry, courseEntry,
    yearnsecEntry, userEntry, passEntry, cpassEntry, register
):
    """Handle the user registration process."""
    first_name = fNameEntry.get().lower()
    last_name = lNameEntry.get().lower()
    student_id = studentIDEntry.get().lower()
    course = courseEntry.get().lower()
    year_section = yearnsecEntry.get().lower()
    username = userEntry.get().lower()
    password = passEntry.get().lower()
    confirm_password = cpassEntry.get().lower()

    if not first_name or not last_name or not student_id or not course or not year_section:
        messagebox.showerror("Error", "All fields are required!")
        return

    if not username or not password or not confirm_password:
        messagebox.showerror("Error", "Username and password fields cannot be empty!")
        return

    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match!")
        return

    success = insert_user(first_name, last_name, student_id, course, year_section, username, password)

    if success:
        messagebox.showinfo("Registration", "Registration successful!")
        open_login(register)
    else:
        messagebox.showerror("Error", "Username or Student ID already taken.")

# Handle user login
def login_user(username_entry, password_entry, login):
    """Handle the user login process."""
    username = username_entry.get().lower()
    password = password_entry.get().lower()

    if username == 'username' or password == 'password':
        messagebox.showerror("Error", "Please enter your username and password!")
        return

    if verify_user(username, password):
        messagebox.showinfo("Login", "Login successful!")
        open_student_dashboard(login)
    else:
        messagebox.showerror("Error", "Invalid username or password!")

# Handle admin login
def admin_user(userEntry, passEntry, admin):
    """Handle the admin login process."""
    username = userEntry.get().lower()
    password = passEntry.get().lower()

    if username == 'username' or password == 'password':
        messagebox.showerror("Error", "Please enter your username and password!")
        return

    if verify_admin(username, password):
        messagebox.showinfo("Admin", "Admin login successful!")
        openadmindash(admin)
    else:
        messagebox.showerror("Error", "Invalid admin username or password!")

# ------------------ Navigation Functions ------------------

# Open the student dashboard
def open_student_dashboard(login):
    """Open the student dashboard."""
    login.destroy()
    studentdash.open_student_dashboard()

# Open the admin dashboard
def openadmindash(admin):
    """Open the admin dashboard."""
    admin.destroy()
    admindash.open_admin_dashboard()

# Open the login form from the registration form
def open_login(register):
    """Open the login form from the registration form."""
    register.destroy()
    loginform.open_loginform()

# Open the registration form from the login form
def open_register(login):
    """Open the registration form from the login form."""
    login.destroy()
    registerform.open_registerform()

# Open the admin login form
def open_admin(login):
    """Open the admin login form from the regular login form."""
    login.destroy()
    adminloginform.open_adminform()

# Close a window
def close_window(window):
    """Close the specified window."""
    window.destroy()

# ------------------ Initialize Database ------------------

# Create tables when the script is run for the first time
create_tables()
