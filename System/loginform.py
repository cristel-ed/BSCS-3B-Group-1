from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import registerform
import adminloginform
import db_connection

# Create the login window
def open_loginform():
    login = Tk()
    login.geometry('1024x720+180+0')
    login.overrideredirect(True)
    login.title('Login Page')

    # Add background image
    backgroundImage = PhotoImage(file='Image/LoginPage.png')
    bg_label = Label(login, image=backgroundImage)
    bg_label.place(x=0, y=0)

    def view_pass():
        hidePass.config(file='Image/view.png')
        passEntry.config(show='')
        eye_button.config(command=hide_pass)

    def hide_pass():
        hidePass.config(file='Image/hide.png')
        passEntry.config(show='*')
        eye_button.config(command=view_pass)


    def openregister():
        login.destroy()  # Close the current login form
        registerform.open_registerform()  # Open the register form

    def openadmin():
        login.destroy()  # Close login form
        adminloginform.open_adminform()  # Open admin login form

    def login_user():
        """Fetch the form data and verify user credentials."""
        username = userEntry.get().lower()
        password = passEntry.get().lower()

        if username == 'username' or password == 'password':
            messagebox.showerror("Error", "Please enter your username and password!")
            return

        # Call the function to verify credentials using SQLite3
        if db_connection.verify_user(username, password):
            messagebox.showinfo("Login", "Login successful!")
            # Proceed to next part of the application (e.g., open user dashboard)
        else:
            messagebox.showerror("Error", "Invalid username or password!")

    # User entry field with placeholder
    userEntry = Entry(login, width=19, font=('Arial Rounded MT Bold', 20), bd=0, bg='#ADD1FB', fg='#000000')
    userEntry.place(x=568, y=316)

    # Password entry field with placeholder and hidden text
    passEntry = Entry(login, width=19, font=('Arial Rounded MT Bold', 20), bd=0, bg='#ADD1FB', fg='#000000')
    passEntry.place(x=568, y=435)


    # Submit button
    loginButton = Button(login, width=8, text='Submit', font=('Arial Rounded MT Bold', 15), bd=0, bg='#ADD1FB',activebackground='#ADD1FB', cursor='hand2', command=login_user)
    loginButton.place(x=666, y=520)

    # Sign-up button
    signupButton = Button(login, width=6, text='Sign up', font=('Arial Rounded MT Bold', 12), bd=0, bg='#ffffff',activebackground='#ffffff', fg='#50C2C9', activeforeground='#50C2C9', cursor='hand2',command=openregister)
    signupButton.place(x=795, y=594)

    # Admin login button with image
    adminImage = PhotoImage(file='Image/AdminButton.png')
    adminButton = Button(login, image=adminImage, bd=0, bg='#FBADAD', activebackground='#FBADAD', cursor='hand2',command=openadmin)
    adminButton.place(x=900, y=630)

    # Toggle show/hide password functionality
    hidePass = PhotoImage(file='Image/hide.png')
    eye_button = Button(login, image=hidePass, bd=0, bg='#ADD1FB', activebackground='#ADD1FB', cursor='hand2', command=view_pass)
    eye_button.place(x=885, y=440)


    def close_window():
        login.destroy()

    # Create a custom close button (X)
    xImage = PhotoImage(file='Image/X-ICon.png')
    close_button = Button(login, image=xImage, command=close_window, bg='#FBADAD', fg='#000000',activebackground='#FBADAD', font=('Arial', 10) , bd=0, cursor='hand2')
    close_button.place(x=973, y=22)

    login.mainloop()

if __name__ == '__main__':
    open_loginform()
