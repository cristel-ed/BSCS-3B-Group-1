from tkinter import *
from PIL import ImageTk
import register_form  # Import the register_form.py module

# Create the login window
def open_login_form():
    login = Tk()
    login.geometry('900x660+200+15')
    login.resizable(0, 0)
    login.title('Login Page')

    # Add background image
    bgImage = PhotoImage(file='Image/LoginFormBg.png')
    bg_label = Label(login, image=bgImage)
    bg_label.place(x=0, y=0)

    # Functions to show and hide password
    def view_pass():
        hidepass.config(file='Image/view.png')
        passEntry.config(show='')
        eye_button.config(command=hide_pass)

    def hide_pass():
        hidepass.config(file='Image/hide.png')
        passEntry.config(show='*')
        eye_button.config(command=view_pass)

    # Function to clear default text in username field
    def use_enter(event):
        if userEntry.get() == 'username':
            userEntry.delete(0, END)

    # Function to clear default text in password field
    def use_pass(event):
        if passEntry.get() == 'password':
            passEntry.config(show='*')
            passEntry.delete(0, END)

    # Function to open the registration form and close the login form
    def open_register():
        login.destroy()  # Close the current login form
        register_form.open_register_form()  # Open the register form

    # Heading labels
    heading = Label(login, text='Evaluation System', font=('Arial Rounded MT Bold', 23, 'bold'), bg='#C2C1C1', fg='#000000')
    heading.place(x=445, y=120)
    heading = Label(login, text='Login Form', font=('Arial Rounded MT Bold', 15), bg='#C2C1C1', fg='#000000')
    heading.place(x=530, y=170)
    heading = Label(login, text='Username', font=('Arial Rounded MT Bold', 15), bg='#C2C1C1', fg='#000000')
    heading.place(x=430, y=270)
    heading = Label(login, text='Password', font=('Arial Rounded MT Bold', 15), bg='#C2C1C1', fg='#000000')
    heading.place(x=430, y=350)

    # Username entry field
    userEntry = Entry(login, width=23, font=('Arial Rounded MT Bold', 12), bd=0, bg='#C2C1C1', fg='#747474')
    userEntry.place(x=440, y=310)
    userEntry.insert(0, 'username')
    userEntry.bind('<FocusIn>', use_enter)
    Frame(login, width=285, height=2, bg='#81B9CB').place(x=440, y=335)

    # Password entry field
    passEntry = Entry(login, width=24, font=('Arial Rounded MT Bold', 12), bd=0, bg='#C2C1C1', fg='#747474')
    passEntry.place(x=440, y=390)
    passEntry.insert(0, 'password')
    passEntry.bind('<FocusIn>', use_pass)
    Frame(login, width=285, height=2, bg='#81B9CB').place(x=440, y=415)

    # Eye button for showing/hiding password
    hidepass = PhotoImage(file='Image/hide.png')
    eye_button = Button(login, image=hidepass, bd=0, bg='#C2C1C1', cursor='hand2', command=view_pass)
    eye_button.place(x=690, y=380)

    # Login button
    loginButton = Button(login, width=20, text='Submit', font=('Arial Rounded MT Bold', 12), bg='#12D0C5', activebackground='#12D0C5', fg='#000000', activeforeground='#000000', cursor='hand2')
    loginButton.place(x=475, y=450)

    # Register button to open the registration form
    registerButton = Button(login, width=15, text='Create an Account', font=('Arial Rounded MT Bold', 10), bd=0, bg='#C2C1C1', activebackground='#C2C1C1', fg='#000000', activeforeground='#000000', cursor='hand2', command=open_register)
    registerButton.place(x=520, y=500)

    # Start the login window
    login.mainloop()

if __name__ == '__main__':
    open_login_form()