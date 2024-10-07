from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import db_connection  # Assuming this module handles SQLite3 database interactions
import loginform

# Create the admin window
def open_adminform():
    admin = Tk()
    admin.geometry('1024x720+180+0')
    admin.overrideredirect(True)
    admin.title('Register Page')

    # Add background image
    backgroundImage = PhotoImage(file='Image/AdminLoginPage.png')
    bg_label = Label(admin, image=backgroundImage)
    bg_label.place(x=0, y=0)

    def view_pass():
        hidePass.config(file='Image/view.png')
        passEntry.config(show='')
        eye_button.config(command=hide_pass)

    def hide_pass():
        hidePass.config(file='Image/hide.png')
        passEntry.config(show='*')
        eye_button.config(command=view_pass)


    def openlogin():
        admin.destroy()  # Close the current admin form
        loginform.open_loginform()  # Open the login form

    def admin_user():
        """Fetch the form data and verify admin credentials."""
        username = userEntry.get().lower()
        password = passEntry.get().lower()

        if username == 'username' or password == 'password':
            messagebox.showerror("Error", "Please enter your username and password!")
            return

        # Call the function to verify admin credentials using SQLite3
        if db_connection.verify_admin(username, password):
            messagebox.showinfo("Admin", "Admin login successful!")
            # Proceed to the next part of your admin application
        else:
            messagebox.showerror("Error", "Invalid admin username or password!")

    userEntry = Entry(admin, width=19, font=('Arial Rounded MT Bold', 20), bd=0, bg='#ADD1FB', fg='#000000')
    userEntry.place(x=568, y=316)


    passEntry = Entry(admin, width=19, font=('Arial Rounded MT Bold', 20), bd=0, bg='#ADD1FB', fg='#000000',show='*')
    passEntry.place(x=568, y=435)


    adminButton = Button(admin, width=8, text='Submit', font=('Arial Rounded MT Bold', 15), bd=0, bg='#ADD1FB',activebackground='#ADD1FB', cursor='hand2', command=admin_user)
    adminButton.place(x=666, y=520)

    signupButton = Button(admin, width=9, text='Login Here', font=('Arial Rounded MT Bold', 12), bd=0, bg='#ffffff',activebackground='#ffffff', fg='#50C2C9', activeforeground='#50C2C9', cursor='hand2',command=openlogin)
    signupButton.place(x=765, y=594)

    hidePass = PhotoImage(file='Image/hide.png')
    eye_button = Button(admin, image=hidePass, bd=0, bg='#ADD1FB', activebackground='#ADD1FB', cursor='hand2',command=view_pass)
    eye_button.place(x=885, y=440)

    def close_window():
        admin.destroy()

    # Create a custom close button (X)
    xImage = PhotoImage(file='Image/X-ICon.png')
    close_button = Button(admin, image=xImage, command=close_window, bg='#FBADAD', fg='#000000',activebackground='#FBADAD', font=('Arial', 10) , bd=0, cursor='hand2')
    close_button.place(x=973, y=22)

    admin.mainloop()

