from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
from loginform import open_loginform
import db_connection


# Create the admin window
def open_adminform():
    admin = Tk()
    admin.geometry('320x480')
    admin.resizable(0, 0)
    admin.title('admin Page')

    # Add background image
    backgroundImage = PhotoImage(file='Image/AdminLoginPage.png')
    bg_label = Label(admin, image=backgroundImage)
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

    def openlogin():
        admin.destroy()  # Close the current admin form
        open_loginform() # Open the login form

    def admin_user():
        """Fetch the form data and verify admin credentials."""
        username = userEntry.get().lower()
        password = passEntry.get().lower()

        if username == 'username' or password == 'password':
            messagebox.showerror("Error", "Please enter your username and password!")
            return

        # Call the function to verify admin credentials
        if db_connection.verify_admin(username, password):
            messagebox.showinfo("Admin", "Admin login successful!")
            # Proceed to the next part of your admin application
        else:
            messagebox.showerror("Error", "Invalid admin username or password!")

    userEntry = Entry(admin, width=13, font=('Arial Rounded MT Bold', 12), bd=0, bg='#ADD1FB', fg='#000000')
    userEntry.place(x=97, y=243.5)
    create_placeholder_entry(userEntry, 'Username')
    passEntry = Entry(admin, width=13, font=('Arial Rounded MT Bold', 12), bd=0, bg='#ADD1FB', fg='#000000')
    passEntry.place(x=97, y=316.5)
    create_placeholder_entry(passEntry, 'Password', is_password=True)

    adminButton = Button(admin, width=18, text='Submit', font=('Arial Rounded MT Bold', 8), bd=0, bg='#ADD1FB', activebackground='#ADD1FB', cursor='hand2', command=admin_user)
    adminButton.place(x=95, y=376)

    signupButton = Button(admin, width=8, text='Login Here', font=('Arial Rounded MT Bold', 7), bd=0, bg='#ffffff', activebackground='#ffffff', fg='#50C2C9', activeforeground='#50C2C9', cursor='hand2', command=openlogin)
    signupButton.place(x=193, y=428)

    hidePass = PhotoImage(file='Image/hide16x16.png')
    eye_button = Button(admin, image=hidePass, bd=0, bg='#ADD1FB', activebackground='#ADD1FB', cursor='hand2', command=view_pass)
    eye_button.place(x=230, y=318)


    admin.mainloop()
