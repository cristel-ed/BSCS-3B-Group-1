import tkinter as tk
from functions import navigation
from functions import admin_dashboard_functions as adf

def open_admin_dashboard():
    """Admin dashboard to manage and assign Google Forms."""
    admin_window = tk.Tk()
    admin_window.geometry("900x600")
    admin_window.title("Admin Dashboard")

    # Create a frame for the menu
    menu_frame = tk.Frame(admin_window, width=200, bg="#f0f0f0")
    menu_frame.pack(side=tk.LEFT, fill=tk.Y)

    # Create a frame for the main content
    main_frame = tk.Frame(admin_window, bg="#ffffff")
    main_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    # Logout Button
    def logout():
        navigation.open_admin_login(admin_window)

    # Menu Buttons
    tk.Button(menu_frame, text="Manage Forms", command=lambda: adf.show_forms(main_frame), width=20, height=2).pack(pady=10)
    tk.Button(menu_frame, text="Professors", command=lambda: adf.show_professors(main_frame), width=20, height=2).pack(pady=10)
    tk.Button(menu_frame, text="Logout", command=logout, width=20, height=2).pack(pady=10)

    # Show the forms list on launch
    adf.show_forms(main_frame)

    admin_window.mainloop()


