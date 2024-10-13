import tkinter as tk
from tkinter import messagebox, Listbox, Scrollbar, Frame, simpledialog
from .forms_database import get_all_forms, insert_form, assign_form_to_all_students,delete_professor
from .database import get_all_professors, insert_professor # Ensure delete_professor is imported

def clear_main_frame(main_frame):
    """Clear the main frame of widgets."""
    for widget in main_frame.winfo_children():
        widget.destroy()

def show_forms(main_frame):
    """Show forms in the main frame as buttons."""
    clear_main_frame(main_frame)

    tk.Label(main_frame, text="List of Created Forms", font=("Arial", 16)).pack(pady=10)

    # Fetch and display forms as buttons
    forms = get_all_forms()  # [(id, form_url, form_name), ...]
    for form in forms:
        form_id, form_url, form_name = form  # Unpack the new structure
        tk.Button(main_frame, text=form_name, font=("Arial", 14), width=50,
                  command=lambda f=form: open_assign_form_view(f, main_frame)).pack(pady=5)

    # Button to create a new form
    tk.Button(main_frame, text="Create New Form", command=lambda: create_form_frame(main_frame), width=20).pack(pady=10)

def create_form_frame(main_frame):
    """Create a new form entry frame."""
    clear_main_frame(main_frame)

    tk.Label(main_frame, text="Create New Form", font=("Arial", 16)).pack(pady=10)

    # Form Name input
    tk.Label(main_frame, text="Enter Form Name:", font=("Arial", 14)).pack(pady=5)
    form_name_entry = tk.Entry(main_frame, font=("Arial", 14), width=50)
    form_name_entry.pack(pady=5)

    # Form URL input
    tk.Label(main_frame, text="Enter Google Form URL:", font=("Arial", 14)).pack(pady=5)
    form_url_entry = tk.Entry(main_frame, font=("Arial", 14), width=50)
    form_url_entry.pack(pady=5)

    # Confirm creation button
    tk.Button(main_frame, text="Create Form",
              command=lambda: create_form(form_url_entry.get(), form_name_entry.get(), main_frame)).pack(pady=10)

    # Back to forms button
    tk.Button(main_frame, text="Back to Forms", command=lambda: show_forms(main_frame), width=20).pack(pady=10)

def create_form(form_url, form_name, main_frame):
    """Create a new form in the database."""
    if not form_url:
        messagebox.showerror("Error", "Form URL is required!")
        return

    if not form_name:
        messagebox.showerror("Error", "Form Name is required!")
        return

    if insert_form(form_url, form_name):
        messagebox.showinfo("Success", "Form created successfully!")
        show_forms(main_frame)  # Refresh the forms list
    else:
        messagebox.showerror("Error", "Failed to create form. It may already exist.")

def open_assign_form_view(selected_form, main_frame):
    """Open the form assignment view for a selected form."""
    clear_main_frame(main_frame)
    form_id, form_url, form_name = selected_form  # Unpack all three values

    # Display selected form information
    tk.Label(main_frame, text=f"Assign Form: {form_name}", font=("Arial", 16)).pack(pady=10)

    # Create a frame for professor selection
    professor_listbox, get_selected_professors = create_professor_selection_list(main_frame)

    # Due date input
    tk.Label(main_frame, text="Enter Due Date (YYYY-MM-DD):", font=("Arial", 14)).pack(pady=5)
    due_date_entry = tk.Entry(main_frame, font=("Arial", 14), width=50)
    due_date_entry.pack(pady=5)

    # Confirm assignment button
    tk.Button(main_frame, text="Confirm Assignment",
              command=lambda: confirm_assignment(form_url, get_selected_professors, due_date_entry.get(), main_frame)).pack(pady=10)

def confirm_assignment(form_url, get_selected_professors, due_date, main_frame):
    """Confirm form assignment to selected professors and students."""
    selected_professors = get_selected_professors()
    if not selected_professors:
        messagebox.showerror("Error", "At least one professor must be selected!")
        return

    if not due_date:
        messagebox.showerror("Error", "Due date is required!")
        return

    assign_to_all = messagebox.askyesno("Confirm Assignment", "Do you want to assign this form to all students?")
    if not assign_to_all:
        return

    # Assign the form to each selected professor separately
    for professor in selected_professors:
        success = assign_form_to_all_students(form_url, professor, due_date)
        if not success:
            messagebox.showerror("Error", f"Failed to assign form to {professor}.")
            return  # Stop if one assignment fails

    messagebox.showinfo("Success", "Forms assigned to selected professors successfully!")
    show_forms(main_frame)  # Return to the forms list

def create_professor_selection_list(parent):
    """Create professor selection list."""
    tk.Label(parent, text="Select Professors", font=("Arial", 14)).pack(pady=(10, 0))

    list_frame = Frame(parent)
    list_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    scrollbar = Scrollbar(list_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    professor_listbox = Listbox(list_frame, selectmode=tk.MULTIPLE, font=("Arial", 14),
                                yscrollcommand=scrollbar.set)
    professor_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar.config(command=professor_listbox.yview)

    professors = get_all_professors()
    for index, professor in enumerate(professors, start=1):
        professor_listbox.insert(tk.END, f"{index}. {professor}")

    return professor_listbox, lambda: [professor_listbox.get(i)[3:] for i in professor_listbox.curselection()]

def show_professors(main_frame):
    """Display the professor management view."""
    clear_main_frame(main_frame)

    tk.Label(main_frame, text="List of Professors", font=("Arial", 16)).pack(pady=10)

    # Create a frame for the professor selection list
    professor_listbox, get_selected_professors = create_professor_selection_list(main_frame)

    # Frame for horizontal button arrangement
    button_frame = Frame(main_frame)
    button_frame.pack(pady=10)

    # Buttons for professor management actions
    tk.Button(button_frame, text="Add Professor", command=lambda: add_professor(main_frame), width=20, font=("Arial", 12)).pack(side=tk.LEFT, padx=10, pady=10)
    tk.Button(button_frame, text="View Professor's Performance",
              command=lambda: view_professor(get_selected_professors()), width=25, font=("Arial", 12)).pack(side=tk.LEFT, padx=10, pady=10)
    tk.Button(button_frame, text="Delete Selected Professor",
              command=lambda: delete_professors(get_selected_professors(), main_frame), width=25, font=("Arial", 12)).pack(side=tk.LEFT, padx=10, pady=10)

def view_professor(selected_professors):
    """View details of a selected professor."""
    if not selected_professors:
        messagebox.showerror("Error", "No professor selected!")
        return
    professor_name = selected_professors[0]  # Get the first selected professor
    messagebox.showinfo("Professor Details", f"Selected Professor: {professor_name}")

def delete_professors(selected_professors, main_frame):
    """Delete selected professor."""
    if not selected_professors:
        messagebox.showerror("Error", "No professor selected for deletion.")
        return

    # Confirm deletion
    confirm = messagebox.askyesno("Confirm Deletion",
                                  f"Are you sure you want to delete the selected professor(s): {', '.join(selected_professors)}?")
    if not confirm:
        return

    # Delete each selected professor
    for professor in selected_professors:
        if delete_professor(professor):  # Ensure the correct function is used here
            messagebox.showinfo("Success", f"Professor '{professor}' deleted successfully.")
        else:
            messagebox.showerror("Error", f"Failed to delete professor '{professor}'. It may not exist.")

    # Refresh the professor list
    show_professors(main_frame)

def add_professor(main_frame):
    """Add a new professor."""
    professor_name = tk.simpledialog.askstring("Add Professor", "Enter Professor Name:")
    if not professor_name:
        messagebox.showerror("Error", "Professor name is required!")
        return

    if insert_professor(professor_name):
        messagebox.showinfo("Success", f"Professor '{professor_name}' added successfully!")
        show_professors(main_frame)
    else:
        messagebox.showerror("Error", "Professor already exists or an error occurred.")
