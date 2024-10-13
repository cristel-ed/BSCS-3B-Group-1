import tkinter as tk
from tkinter import messagebox
from .database import create_connection
import webbrowser
from datetime import datetime

def show_home(main_frame, first_name, student_id):
    """Display home section with greeting and pending forms count."""
    clear_main_frame(main_frame)
    greeting_label = tk.Label(main_frame, text=f"Welcome, {first_name}!", font=("Arial", 18))
    greeting_label.pack(pady=20)

    # Display the number of pending evaluation forms
    conn = create_connection()
    if conn is None:
        messagebox.showerror("Error", "Failed to connect to the database.")
        return

    try:
        c = conn.cursor()
        c.execute("SELECT COUNT(*) FROM AssignedForms WHERE student_id = ? AND completed = 0", (student_id,))
        pending_count = c.fetchone()[0]
        pending_label = tk.Label(main_frame, text=f"Pending Evaluation Forms: {pending_count}", font=("Arial", 16))
        pending_label.pack(pady=10)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load pending forms count: {e}")
    finally:
        conn.close()

def clear_main_frame(main_frame):
    """Clear the main frame of the student dashboard."""
    for widget in main_frame.winfo_children():
        widget.destroy()

def load_assigned_forms(main_frame, student_id, selection):
    """Load and display assigned forms based on selection (Pending or Completed)."""
    conn = create_connection()
    if conn is None:
        messagebox.showerror("Error", "Failed to connect to the database.")
        return

    try:
        c = conn.cursor()
        query = ("SELECT professor_name, due_date, form_url FROM AssignedForms "
                 "WHERE student_id = ? AND completed = ?")
        status = 0 if selection == "Pending Forms" else 1
        c.execute(query, (student_id, status))

        forms = c.fetchall()
        clear_main_frame(main_frame)

        if not forms:
            tk.Label(main_frame, text=f"No {selection.lower()}.", font=("Arial", 16)).pack(pady=20)
        else:
            tk.Label(main_frame, text=f"{selection}:", font=("Arial", 16)).pack(pady=10)

            for professor_name, due_date, form_url in forms:
                due_date_str = datetime.strptime(due_date, '%Y-%m-%d').strftime('%B %d, %Y')
                form_button = tk.Button(
                    main_frame, text=f"{professor_name}           Due: {due_date_str}",
                    command=lambda url=form_url: open_form(url) if status else
                    show_form_details(main_frame, professor_name, due_date, form_url, student_id),
                    width=40, height=2
                )
                form_button.pack(pady=5)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load forms: {e}")
    finally:
        conn.close()

def show_form_details(main_frame, professor_name, due_date, form_url, student_id):
    """Display details for a specific form."""
    clear_main_frame(main_frame)
    tk.Label(main_frame, text=f"Evaluating Professor: {professor_name}", font=("Arial", 16)).pack(pady=10)
    tk.Label(main_frame, text=f"Due Date: {due_date}", font=("Arial", 16)).pack(pady=10)

    evaluate_button = tk.Button(main_frame, text="Evaluate", command=lambda: open_form(form_url), width=20)
    evaluate_button.pack(pady=10)

    complete_button = tk.Button(main_frame, text="Mark as Completed",
                                command=lambda: mark_form_as_completed(professor_name, student_id), width=20)
    complete_button.pack(pady=10)

def open_form(form_url):
    """Open the specified form URL."""
    if form_url:
        webbrowser.open(form_url)
    else:
        messagebox.showerror("Error", "Form URL not found.")

def mark_form_as_completed(professor_name, student_id):
    """Mark a form as completed for the given professor and student."""
    conn = create_connection()
    if conn is None:
        messagebox.showerror("Error", "Failed to connect to the database.")
        return

    try:
        c = conn.cursor()
        c.execute("UPDATE AssignedForms SET completed = 1, pending = 0 WHERE professor_name = ? AND student_id = ? AND completed = 0",
                  (professor_name, student_id))
        conn.commit()

        if c.rowcount == 0:
            messagebox.showwarning("Warning", "No form was marked as completed. Please check the professor name.")
        else:
            messagebox.showinfo("Success", "Form marked as completed.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to mark form as completed: {e}")
    finally:
        conn.close()
