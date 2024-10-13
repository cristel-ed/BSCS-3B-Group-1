# user_auth.py
import sqlite3
from tkinter import messagebox
import loginform
import studentdash
import admindash

def register_user(fNameEntry, lNameEntry, studentIDEntry, courseEntry,
                  yearnsecEntry, userEntry, passEntry, cpassEntry, register):
    from .navigation import open_login
    """Handle the user registration process."""
    from .user import insert_user  # Import here
    first_name = fNameEntry.get().lower()
    last_name = lNameEntry.get().lower()
    student_id = studentIDEntry.get().lower()
    course = courseEntry.get().lower()
    year_section = yearnsecEntry.get().lower()
    username = userEntry.get().lower()
    password = passEntry.get().lower()
    confirm_password = cpassEntry.get().lower()

    if not all([first_name, last_name, student_id, course, year_section, username, password, confirm_password]):
        messagebox.showerror("Error", "All fields are required!")
        return

    if password != confirm_password:
        messagebox.showerror("Error", "Passwords do not match!")
        return

    if insert_user(first_name, last_name, student_id, course, year_section, username, password):
        messagebox.showinfo("Registration", "Registration successful!")
        open_login(register)
    else:
        messagebox.showerror("Error", "Username or Student ID already taken.")

def login_user(username_entry, password_entry, login):
    """Handle the user login process."""
    from .user import verify_user  # Import here
    from .navigation import open_student_dashboard  # Import here
    username = username_entry.get().lower()
    password = password_entry.get().lower()

    if username == 'username' or password == 'password':
        messagebox.showerror("Error", "Please enter your username and password!")
        return

    student_id = verify_user(username, password)
    if student_id:
        messagebox.showinfo("Login", "Login successful!")
        open_student_dashboard(login, student_id)
    else:
        messagebox.showerror("Error", "Invalid username or password!")

def admin_user(userEntry, passEntry, admin):
    """Handle the admin login process."""
    from .admin import verify_admin
    from .navigation import open_admin_dashboard
    username = userEntry.get().lower()
    password = passEntry.get().lower()

    if username == 'username' or password == 'password':
        messagebox.showerror("Error", "Please enter your username and password!")
        return

    if verify_admin(username, password):
        messagebox.showinfo("Admin", "Admin login successful!")
        open_admin_dashboard(admin)
    else:
        messagebox.showerror("Error", "Invalid admin username or password!")
