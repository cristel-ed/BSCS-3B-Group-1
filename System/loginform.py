from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import registerform
import adminloginform
import db_connection

# Create the login window
def open_loginform():
    login = Tk()
    login.geometry('320x480')
    login.resizable(0, 0)
    login.title('Login Page')

    # Add background image
    backgroundImage = PhotoImage(file='Image/LoginFormMobile.png')
    bg_label = Label(login, image=backgroundImage)
    bg_label.place(x=0, y=0)

    def view_pass():
        hidePass.config(file='Image/view16x16.png')
        passEntry.config(show='')
        eye_button.config(command=hide_pass)

    def hide_pass():
        hidePass.config(file='Image/hide16x16.png')
        passEntry.config(show='*')
        eye_button.config(command=view_pass)

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

    def openregister():
        login.destroy()  # Close the current login form
        registerform.open_registerform() # Open the register form
    def openadmin():
        login.destroy()
        adminloginform.open_adminform()


    def login_user():
        """Fetch the form data and verify user credentials."""
        username = userEntry.get().lower()
        password = passEntry.get().lower()

        if username == 'username' or password == 'password':
            messagebox.showerror("Error", "Please enter your username and password!")
            return

        # Call the function to verify credentials
        if db_connection.verify_user(username, password):
            messagebox.showinfo("Login", "Login successful!")
            # You can now proceed to the next part of your application
        else:
            messagebox.showerror("Error", "Invalid username or password!")

    userEntry = Entry(login, width=13, font=('Arial Rounded MT Bold', 12), bd=0, bg='#ADD1FB', fg='#000000')
    userEntry.place(x=97, y=243.5)
    create_placeholder_entry(userEntry, 'Username')
    passEntry = Entry(login, width=13, font=('Arial Rounded MT Bold', 12), bd=0, bg='#ADD1FB', fg='#000000')
    passEntry.place(x=97, y=316.5)
    create_placeholder_entry(passEntry, 'Password', is_password=True)

    loginButton = Button(login, width=18, text='Submit', font=('Arial Rounded MT Bold', 8), bd=0, bg='#ADD1FB', activebackground='#ADD1FB', cursor='hand2', command=login_user)
    loginButton.place(x=95, y=376)
    signupButton = Button(login, width=5, text='Sign up', font=('Arial Rounded MT Bold', 7), bd=0, bg='#ffffff', activebackground='#ffffff', fg='#50C2C9', activeforeground='#50C2C9', cursor='hand2', command=openregister)
    signupButton.place(x=195, y=428)

    adminImage =PhotoImage(file='Image/AdminButton.png')
    adminButton = Button(login, image=adminImage, bd=0, bg='#FBADAD', activebackground='#FBADAD', cursor='hand2',command=openadmin)
    adminButton.place(x=258, y=424)

    hidePass = PhotoImage(file='Image/hide16x16.png')
    eye_button = Button(login, image=hidePass, bd=0, bg='#ADD1FB', activebackground='#ADD1FB', cursor='hand2', command=view_pass)
    eye_button.place(x=230, y=318)

    login.mainloop()

if __name__ == '__main__':
    open_loginform()