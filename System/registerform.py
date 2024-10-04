#registerform.py
from tkinter import *
from tkinter import messagebox

from PIL import ImageTk

from System import db_connection
from System.loginform import open_loginform


# Create the register window
def open_registerform():
    register = Tk()
    register.geometry('320x480')
    register.resizable(0, 0)
    register.title('register Page')

    # Add background image
    backgroundImage = PhotoImage(file='Image/registerFormMobile.png')
    bg_label = Label(register, image=backgroundImage)
    bg_label.place(x=0, y=0)

    def view_pass():
        hidePass.config(file='Image/view16x16.png')
        passEntry.config(show='')
        eye_button.config(command=hide_pass)

    def hide_pass():
        hidePass.config(file='Image/hide16x16.png')
        passEntry.config(show='*')
        eye_button.config(command=view_pass)

    def view_pass2():
        hidePass2.config(file='Image/view16x16.png')
        cpassEntry.config(show='')
        eye_button2.config(command=hide_pass2)

    def hide_pass2():
        hidePass2.config(file='Image/hide16x16.png')
        cpassEntry.config(show='*')
        eye_button2.config(command=view_pass2)

    def create_placeholder_entry(entry, placeholder_text, is_password=False):
        def focus_in(event):
            if entry.get() == placeholder_text:
                entry.delete(0, END)
                entry.config(fg='#000000')
            if is_password:
                entry.config(show='*')

        def focus_out(event):
            if entry.get() == '':
                if is_password:
                    entry.config(show='*')
                    entry.insert(0, placeholder_text)
                    entry.config(fg='#747474')
                    entry.config(show='')
                else:
                    entry.insert(0, placeholder_text)
                    entry.config(fg='#747474')

        if is_password:
            entry.insert(0, placeholder_text)
            entry.config(fg='#747474')
        else:
            entry.insert(0, placeholder_text)
            entry.config(fg='#747474')

        entry.bind('<FocusIn>', focus_in)
        entry.bind('<FocusOut>', focus_out)

    def open_login():
        register.destroy()  # Close the current register form
        open_loginform()

    # Create entry fields
    fNameEntry = Entry(register, width=9, font=('Arial Rounded MT Bold', 10), bd=0, bg='#ADD1FB', fg='#000000')
    fNameEntry.place(x=76, y=206)
    create_placeholder_entry(fNameEntry, 'First Name')

    lNameEntry = Entry(register, width=9, font=('Arial Rounded MT Bold', 10), bd=0, bg='#ADD1FB', fg='#000000')
    lNameEntry.place(x=172, y=206)
    create_placeholder_entry(lNameEntry, 'Last Name')

    studentIDEntry = Entry(register, width=21, font=('Arial Rounded MT Bold', 10), bd=0, bg='#ADD1FB', fg='#000000')
    studentIDEntry.place(x=76,y=236)
    create_placeholder_entry(studentIDEntry, 'Student ID')

    courseEntry = Entry(register, width=6, font=('Arial Rounded MT Bold', 10), bd=0, bg='#ADD1FB', fg='#000000')
    courseEntry.place(x=76,y=267)
    create_placeholder_entry(courseEntry, 'Course')

    yearnsecEntry = Entry(register, width=12, font=('Arial Rounded MT Bold', 10), bd=0, bg='#ADD1FB', fg='#000000')
    yearnsecEntry.place(x=150,y=267)
    create_placeholder_entry(yearnsecEntry, 'Year & Section')

    userEntry = Entry(register, width=21, font=('Arial Rounded MT Bold', 10), bd=0, bg='#ADD1FB', fg='#000000')
    userEntry.place(x=76,y=298.5)
    create_placeholder_entry(userEntry, 'Username')

    passEntry = Entry(register, width=21, font=('Arial Rounded MT Bold', 10), bd=0, bg='#ADD1FB', fg='#000000')
    passEntry.place(x=76,y=329)
    create_placeholder_entry(passEntry, 'Password', is_password=True)

    cpassEntry = Entry(register, width=21, font=('Arial Rounded MT Bold', 10), bd=0, bg='#ADD1FB', fg='#000000')
    cpassEntry.place(x =76,y=359.5)
    create_placeholder_entry(cpassEntry, 'Confirm Password', is_password=True)

    def register_user():
        """Fetch the form data, convert to lowercase, validate, and register the user."""
        first_name = fNameEntry.get().lower()
        last_name = lNameEntry.get().lower()
        student_id = studentIDEntry.get().lower()
        course = courseEntry.get().lower()
        year_section = yearnsecEntry.get().lower()
        username = userEntry.get().lower()
        password = passEntry.get().lower()
        confirm_password = cpassEntry.get().lower()

        # Check if any field is empty
        if not first_name or first_name == "first name":
            messagebox.showerror("Error", "First Name is required!")
            return
        if not last_name or last_name == "last name":
            messagebox.showerror("Error", "Last Name is required!")
            return
        if not student_id or student_id == "student id":
            messagebox.showerror("Error", "Student ID is required!")
            return
        if not course or course == "course":
            messagebox.showerror("Error", "Course is required!")
            return
        if not year_section or year_section == "year & section":
            messagebox.showerror("Error", "Year & Section is required!")
            return
        if not username or username == "username":
            messagebox.showerror("Error", "Username is required!")
            return
        if not password or password == "password":
            messagebox.showerror("Error", "Password is required!")
            return
        if not confirm_password or confirm_password == "confirm password":
            messagebox.showerror("Error", "Confirm Password is required!")
            return

        # Check if passwords match
        if password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match!")
            return

        # Call the insert_user function from db_connection.py
        success = db_connection.insert_user(first_name, last_name, student_id, course, year_section, username, password)

        if success:
            messagebox.showinfo("Registration", "Registration completed successfully!")
        else:
            messagebox.showerror("Registration", "Username or Student ID already taken. Please try again.")

    registerButton = Button(register, width=18, text='Submit', font=('Arial Rounded MT Bold', 8), bd=0, bg='#ADD1FB', activebackground='#ADD1FB', cursor='hand2', command=register_user)
    registerButton.place(x=95, y=396)
    signupButton = Button(register, width=5, text='Sign in', font=('Arial Rounded MT Bold', 7),bd=0,bg='#ffffff',activebackground='#ffffff',fg='#50C2C9',activeforeground='#50C2C9',cursor='hand2',command=open_login)
    signupButton.place(x=205, y=428)

    hidePass = PhotoImage(file='Image/hide16x16.png')
    eye_button = Button(register, image=hidePass, bd=0, bg='#ADD1FB',activebackground='#ADD1FB', cursor='hand2',command=view_pass)
    eye_button.place(x=230, y=329)

    hidePass2 = PhotoImage(file='Image/hide16x16.png')
    eye_button2 = Button(register, image=hidePass2, bd=0, bg='#ADD1FB',activebackground='#ADD1FB', cursor='hand2',command=view_pass2)
    eye_button2.place(x=230, y=359.5)

    register.mainloop()