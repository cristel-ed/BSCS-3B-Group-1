import studentdash
import admindash
import registerform
import loginform
import adminloginform

def open_student_dashboard(login, student_id):
    """Open the student dashboard with the student ID."""
    login.destroy()
    studentdash.open_student_dashboard(student_id)

def open_admin_dashboard(admin):
    """Open the admin dashboard."""
    admin.destroy()
    admindash.open_admin_dashboard()

def open_admin_login(admin_window):
    """Open the admin login form."""
    admin_window.destroy()
    adminloginform.open_adminform()

def open_login_from_studentdash(student_window):
    """Open the login form from the student dashboard."""
    student_window.destroy()
    loginform.open_loginform()

def open_login(register):
    """Open the login form from the registration form."""
    register.destroy()
    loginform.open_loginform()

def open_register(login):
    """Open the registration form from the login form."""
    login.destroy()
    registerform.open_registerform()

def open_admin(login):
    """Open the admin login form."""
    login.destroy()
    adminloginform.open_adminform()

def close_window(window):
    """Close the specified window."""
    window.destroy()
