# registerform.py
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import db_connection
import loginform

# Create the register window
def open_registerform():
    register = Tk()
    register.geometry('1024x720+180+0')
    register.overrideredirect(True)
    register.title('Register Page')

    # Add background image
    backgroundImage = PhotoImage(file='Image/Signup.png')
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


    def open_login():
        register.destroy()  # Close the current register form
        loginform.open_loginform()

    # Create entry fields
    fNameEntry = Entry(register, width=11, font=('Arial Rounded MT Bold', 20), bd=0, bg='#ADD1FB', fg='#000000')
    fNameEntry.place(x=521, y=158)
    lNameEntry = Entry(register, width=11, font=('Arial Rounded MT Bold', 20), bd=0, bg='#ADD1FB', fg='#000000')
    lNameEntry.place(x=754, y=158)
    studentIDEntry = Entry(register, width=25, font=('Arial Rounded MT Bold', 20), bd=0, bg='#ADD1FB', fg='#000000')
    studentIDEntry.place(x=521, y=243)
    courseEntry = Entry(register, width=11, font=('Arial Rounded MT Bold', 20), bd=0, bg='#ADD1FB', fg='#000000')
    courseEntry.place(x=521, y=327)
    yearnsecEntry = Entry(register, width=11, font=('Arial Rounded MT Bold', 20), bd=0, bg='#ADD1FB', fg='#000000')
    yearnsecEntry.place(x=754, y=327)
    userEntry = Entry(register, width=25, font=('Arial Rounded MT Bold', 20), bd=0, bg='#ADD1FB', fg='#000000')
    userEntry.place(x=521, y=413)
    passEntry = Entry(register, width=25, font=('Arial Rounded MT Bold', 20), bd=0, bg='#ADD1FB', fg='#000000')
    passEntry.place(x=521, y=499)
    cpassEntry = Entry(register, width=25, font=('Arial Rounded MT Bold', 20), bd=0, bg='#ADD1FB', fg='#000000')
    cpassEntry.place(x=521, y=584)

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
            open_login()
        else:
            messagebox.showerror("Registration", "Username or Student ID already taken. Please try again.")

    registerButton = Button(register, width=10, text='Submit', font=('Arial Rounded MT Bold', 14), bd=0, bg='#ADD1FB', activebackground='#ADD1FB', cursor='hand2', command=register_user)
    registerButton.place(x=665, y=641)
    signupButton = Button(register, width=5, text='Sign in', font=('Arial Rounded MT Bold', 12), bd=0, bg='#ffffff',activebackground='#ffffff', fg='#50C2C9', activeforeground='#50C2C9', cursor='hand2',command=open_login)
    signupButton.place(x=810, y=689)

    hidePass = PhotoImage(file='Image/hide.png')
    eye_button = Button(register, image=hidePass, bd=0, bg='#ADD1FB', activebackground='#ADD1FB', cursor='hand2',command=view_pass)
    eye_button.place(x=910, y=503)

    hidePass2 = PhotoImage(file='Image/hide.png')
    eye_button2 = Button(register, image=hidePass2, bd=0, bg='#ADD1FB', activebackground='#ADD1FB', cursor='hand2',command=view_pass2)
    eye_button2.place(x=910, y=587)

    def close_window():
        register.destroy()

    # Create a custom close button (X)
    xImage = PhotoImage(file='Image/X-ICon.png')
    close_button = Button(register, image=xImage, command=close_window, bg='#FBADAD', fg='#000000',activebackground='#FBADAD', font=('Arial', 10) , bd=0, cursor='hand2')
    close_button.place(x=973, y=22)

    register.mainloop()

