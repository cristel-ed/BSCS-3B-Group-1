#studentdash.py
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import loginform

def open_student_dashboard():
    dashboard = tk.Tk()
    dashboard.geometry('1024x720+180+0')
    dashboard.title('Student Dashboard')
    dashboard.overrideredirect(True)
    dashboard.configure(bg='#f0f0f0')

    # Load button images (replace with actual image paths)
    icon_size = (32, 32)  # Standard icon size
    welcome_icon = ImageTk.PhotoImage(Image.open("Image/X-ICon.png").resize(icon_size))
    pending_icon = ImageTk.PhotoImage(Image.open("Image/X-ICon.png").resize(icon_size))
    completed_icon = ImageTk.PhotoImage(Image.open("Image/X-ICon.png").resize(icon_size))
    progress_icon = ImageTk.PhotoImage(Image.open("Image/X-ICon.png").resize(icon_size))
    course_icon = ImageTk.PhotoImage(Image.open("Image/X-ICon.png").resize(icon_size))
    feedback_icon = ImageTk.PhotoImage(Image.open("Image/X-ICon.png").resize(icon_size))
    logout_icon = ImageTk.PhotoImage(Image.open("Image/X-ICon.png").resize(icon_size))

    # Title Label
    title_label = tk.Label(dashboard, text="Student Dashboard", font=('Arial Rounded MT Bold', 30), bg='#f0f0f0')
    title_label.pack(pady=20)

    # Button Frame
    button_frame = tk.Frame(dashboard, bg='#ADD1FB', bd=5, relief=tk.RIDGE)
    button_frame.pack(side=tk.LEFT, fill=tk.Y, padx=5)

    # Main Frame for content
    main_frame = tk.Frame(dashboard, bg='#f0f0f0')
    main_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

    def show_frame(frame):
        for widget in main_frame.winfo_children():
            widget.pack_forget()  # Hide any existing frames
        frame.pack(fill=tk.BOTH, expand=True)

    # Welcome Section Frame
    welcome_frame = tk.Frame(main_frame, bg='#ADD1FB', bd=2, relief=tk.RIDGE)
    welcome_label = tk.Label(welcome_frame, text="Welcome, [Student Name]", font=('Arial Rounded MT Bold', 16), bg='#ADD1FB')
    welcome_label.pack(pady=10)
    profile_image_label = tk.Label(welcome_frame, text="[Profile Picture]", font=('Arial', 14), bg='#ADD1FB')  # Placeholder for profile picture
    profile_image_label.pack(pady=10)
    announcement_label = tk.Label(welcome_frame, text="Announcements:\n- Evaluation Deadline: Oct 20\n- System Update Tomorrow", font=('Arial', 14), bg='#ADD1FB')
    announcement_label.pack()

    # Pending Evaluations Frame
    pending_frame = tk.Frame(main_frame, bg='#ADD1FB', bd=2, relief=tk.RIDGE)
    pending_label = tk.Label(pending_frame, text="Pending Evaluations", font=('Arial Rounded MT Bold', 16), bg='#ADD1FB')
    pending_label.pack(pady=10)
    pending_eval_label = tk.Label(pending_frame, text="Course 1 - Prof A: Due in 5 days\nCourse 2 - Prof B: Due in 2 days", font=('Arial', 14), bg='#ADD1FB')
    pending_eval_label.pack()
    start_eval_button = tk.Button(pending_frame, text="Start Evaluation", font=('Arial Rounded MT Bold', 12), bg='#50C2C9',
                                  command=lambda: messagebox.showinfo("Evaluation", "Starting Evaluation..."))
    start_eval_button.pack(pady=10)

    # Completed Evaluations Frame
    completed_frame = tk.Frame(main_frame, bg='#ADD1FB', bd=2, relief=tk.RIDGE)
    completed_label = tk.Label(completed_frame, text="Completed Evaluations", font=('Arial Rounded MT Bold', 16), bg='#ADD1FB')
    completed_label.pack(pady=10)
    completed_eval_label = tk.Label(completed_frame, text="Course 3 - Prof C: Submitted on Oct 5", font=('Arial', 14), bg='#ADD1FB')
    completed_eval_label.pack()

    # Evaluation Progress Tracker Frame
    progress_frame = tk.Frame(main_frame, bg='#ADD1FB', bd=2, relief=tk.RIDGE)
    progress_label = tk.Label(progress_frame, text="Evaluation Progress", font=('Arial Rounded MT Bold', 16), bg='#ADD1FB')
    progress_label.pack(pady=10)
    progress_bar = tk.ttk.Progressbar(progress_frame, orient="horizontal", length=300, mode="determinate")
    progress_bar.pack(pady=10)
    progress_bar['value'] = 60  # Sample progress value (60%)
    progress_text = tk.Label(progress_frame, text="60% Completed", font=('Arial', 14), bg='#ADD1FB')
    progress_text.pack()

    # Course Information Frame
    course_frame = tk.Frame(main_frame, bg='#ADD1FB', bd=2, relief=tk.RIDGE)
    course_label = tk.Label(course_frame, text="Enrolled Courses", font=('Arial Rounded MT Bold', 16), bg='#ADD1FB')
    course_label.pack(pady=10)
    course_info_label = tk.Label(course_frame, text="Course 1 - Prof A\nCourse 2 - Prof B\nCourse 3 - Prof C", font=('Arial', 14), bg='#ADD1FB')
    course_info_label.pack()

    # General Feedback Submission Frame
    feedback_frame = tk.Frame(main_frame, bg='#ADD1FB', bd=2, relief=tk.RIDGE)
    feedback_label = tk.Label(feedback_frame, text="General Feedback", font=('Arial Rounded MT Bold', 16), bg='#ADD1FB')
    feedback_label.pack(pady=10)
    feedback_textbox = tk.Text(feedback_frame, width=40, height=4)
    feedback_textbox.pack(pady=10)
    submit_feedback_button = tk.Button(feedback_frame, text="Submit Feedback", font=('Arial Rounded MT Bold', 12), bg='#50C2C9',
                                       command=lambda: messagebox.showinfo("Feedback", "Feedback Submitted!"))
    submit_feedback_button.pack(pady=5)

    # Functions to show/hide text on button hover
    def show_text(button, text):
        button.config(text=text, compound=tk.LEFT, padx=10)  # Show text next to image with padding

    def hide_text(button):
        button.config(text='', compound=tk.LEFT)  # Hide text

    # Create buttons in the button frame
    buttons = []

    def create_button(frame, img, command, default_text, hover_text):
        button = tk.Button(frame, image=img, text='', font=('Arial Rounded MT Bold', 12),
                           bg='#ADD1FB', command=command)
        button.pack(anchor='w', pady=10)  # Align to left
        buttons.append((button, hover_text))  # Store button and its hover text
        return button

    # Show the frames as buttons are clicked
    def button_command(frame_index):
        def command():
            show_frame(frames[frame_index])
            highlight_button(buttons[frame_index][0])
        return command

    frames = [welcome_frame, pending_frame, completed_frame, progress_frame, course_frame, feedback_frame]

    create_button(button_frame, welcome_icon, button_command(0), '', 'Welcome')
    create_button(button_frame, pending_icon, button_command(1), '', 'Pending Evaluations')
    create_button(button_frame, completed_icon, button_command(2), '', 'Completed Evaluations')
    create_button(button_frame, progress_icon, button_command(3), '', 'Evaluation Progress')
    create_button(button_frame, course_icon, button_command(4), '', 'Course Information')
    create_button(button_frame, feedback_icon, button_command(5), '', 'General Feedback')

    def logout():
        dashboard.destroy()
        loginform.open_loginform()
    # Logout Button
    logout_button = tk.Button(button_frame, image=logout_icon, text='', font=('Arial Rounded MT Bold', 12),
                              bg='#ADD1FB', command=logout, anchor='w')
    logout_button.pack(anchor='w', pady=10)
    buttons.append((logout_button, 'Logout'))  # Store logout button and its hover text

    # Bind hover events to the button frame
    def show_all_text(event):
        for button, hover_text in buttons:
            show_text(button, hover_text)

    def hide_all_text(event):
        for button, _ in buttons:
            hide_text(button)

    button_frame.bind("<Enter>", show_all_text)  # Show all texts when mouse enters button frame
    button_frame.bind("<Leave>", hide_all_text)  # Hide all texts when mouse leaves button frame

    # Function to highlight the selected button
    def highlight_button(button):
        for btn, _ in buttons:
            btn.config(bg='#ADD1FB')  # Reset background color
        button.config(bg='#50C2C9')  # Highlight selected button

    # Show the initial frame
    show_frame(welcome_frame)
    highlight_button(buttons[0][0])  # Highlight the welcome button by default

    dashboard.mainloop()

if __name__ == '__main__':
    open_student_dashboard()
