import tkinter as tk
from tkinter import messagebox
from functions import database
from functions import navigation
from functions import student_dashboard_functions as sdf  # Import the new functions module

def open_student_dashboard(student_id):
    """Student dashboard to display assigned evaluation forms."""
    student_window = tk.Tk()
    student_window.geometry("800x600")
    student_window.title("Student Dashboard")

    # Fetch the student's first name from the users table
    conn = database.create_connection()
    if conn is None:
        messagebox.showerror("Error", "Failed to connect to the database.")
        return

    try:
        c = conn.cursor()
        c.execute("SELECT first_name FROM users WHERE student_id = ?", (student_id,))
        result = c.fetchone()
        first_name = result[0] if result else f"Student {student_id}"
    except Exception as e:
        messagebox.showerror("Error", f"Failed to retrieve student name: {e}")
        first_name = f"Student {student_id}"  # Fallback if the name isn't found
    finally:
        conn.close()

    # Create frames
    menu_frame = tk.Frame(student_window)
    menu_frame.pack(side=tk.LEFT, fill=tk.Y)

    main_frame = tk.Frame(student_window)
    main_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    def show_home():
        sdf.show_home(main_frame, first_name, student_id)  # Use the new function

    def show_pending_forms():
        sdf.load_assigned_forms(main_frame, student_id, "Pending Forms")  # Use the new function

    def show_completed_forms():
        sdf.load_assigned_forms(main_frame, student_id, "Completed Forms")  # Use the new function

    def clear_main_frame():
        sdf.clear_main_frame(main_frame)  # Use the new function

    def logout():
        navigation.open_login_from_studentdash(student_window)

    def toggle_submenu():
        if submenu_frame.winfo_ismapped():
            submenu_frame.pack_forget()
            logout_button.pack(after=evaluation_button)
        else:
            submenu_frame.pack(side=tk.TOP, fill=tk.Y)
            logout_button.pack(after=submenu_frame)

    home_button = tk.Button(menu_frame, text="Home", command=show_home, width=20, height=2)
    home_button.pack(pady=10)

    evaluation_button = tk.Button(menu_frame, text="Evaluation", command=toggle_submenu, width=20, height=2)
    evaluation_button.pack(pady=10)

    submenu_frame = tk.Frame(menu_frame)
    pending_forms_button = tk.Button(submenu_frame, text="Pending Forms", command=show_pending_forms, width=20)
    pending_forms_button.pack(pady=5)

    completed_forms_button = tk.Button(submenu_frame, text="Completed Forms", command=show_completed_forms, width=20)
    completed_forms_button.pack(pady=5)
    submenu_frame.pack_forget()

    logout_button = tk.Button(menu_frame, text="Logout", command=logout, width=20, height=2)
    logout_button.pack(pady=10)

    show_home()  # Show the home view initially
    student_window.mainloop()

