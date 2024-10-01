from tkinter import *
from PIL import ImageTk

from System.login_form import open_login_form


def open_register_form():
    register = Tk()  # Initialize the Tkinter window
    register.geometry('900x660+200+15')
    register.resizable(0, 0)
    register.title('Register Page')

    # Background Image
    bgImage = PhotoImage(file='Image/LoginFormBg.png')
    bg_label = Label(register, image=bgImage)
    bg_label.place(x=0, y=0)

    # Function to show and hide password
    def view_pass():
        hidePass.config(file='Image/view.png')
        passEntry.config(show='')
        eye_button.config(command=hide_pass)

    def hide_pass():
        hidePass.config(file='Image/hide.png')
        passEntry.config(show='*')
        eye_button.config(command=view_pass)

    def view_pass2():
        hidePass2.config(file='Image/view.png')
        confirmPassEntry.config(show='')
        eye_button2.config(command=hide_pass2)

    def hide_pass2():
        hidePass2.config(file='Image/hide.png')
        confirmPassEntry.config(show='*')
        eye_button2.config(command=view_pass2)

    def open_login():
        register.destroy()  # Close the current register form
        open_login_form()

    # Heading Labels
    heading = Label(register, text='Evaluation System', font=('Arial Rounded MT Bold', 23, 'bold'), bg='#C2C1C1', fg='#000000')
    heading.place(x=445, y=120)

    heading = Label(register, text='Registration Form', font=('Arial Rounded MT Bold', 15), bg='#C2C1C1', fg='#000000')
    heading.place(x=500, y=170)

    heading = Label(register, text='Student Name', font=('Arial Rounded MT Bold', 10), bg='#C2C1C1', fg='#000000')
    heading.place(x=475, y=220)

    heading = Label(register, text='Student ID', font=('Arial Rounded MT Bold', 10), bg='#C2C1C1', fg='#000000')
    heading.place(x=475, y=270)

    heading = Label(register, text='Course', font=('Arial Rounded MT Bold', 10), bg='#C2C1C1', fg='#000000')
    heading.place(x=475, y=320)

    heading = Label(register, text='Year & Section', font=('Arial Rounded MT Bold', 10), bg='#C2C1C1', fg='#000000')
    heading.place(x=600, y=320)

    heading = Label(register, text='Password', font=('Arial Rounded MT Bold', 10), bg='#C2C1C1', fg='#000000')
    heading.place(x=475, y=370)

    heading = Label(register, text='Confirm Password', font=('Arial Rounded MT Bold', 10), bg='#C2C1C1', fg='#000000')
    heading.place(x=475, y=420)

    # Entry Fields
    studentNameEntry = Entry(register, width=24, font=('Arial Rounded MT Bold', 10), bd=0, bg='#C2C1C1', fg='#747474')
    studentNameEntry.place(x=475, y=245)
    Frame(register, width=230, height=2, bg='#81B9CB').place(x=475, y=265)

    studentIDEntry = Entry(register, width=24, font=('Arial Rounded MT Bold', 10), bd=0, bg='#C2C1C1', fg='#747474')
    studentIDEntry.place(x=475, y=295)
    Frame(register, width=230, height=2, bg='#81B9CB').place(x=475, y=315)

    courseEntry = Entry(register, width=12, font=('Arial Rounded MT Bold', 10), bd=0, bg='#C2C1C1', fg='#747474')
    courseEntry.place(x=475, y=345)
    Frame(register, width=100, height=2, bg='#81B9CB').place(x=475, y=365)

    lastnameEntry = Entry(register, width=12, font=('Arial Rounded MT Bold', 10), bd=0, bg='#C2C1C1', fg='#747474')
    lastnameEntry.place(x=600, y=345)
    Frame(register, width=100, height=2, bg='#81B9CB').place(x=600, y=365)

    passEntry = Entry(register, width=24, font=('Arial Rounded MT Bold', 12), bd=0, bg='#C2C1C1', fg='#747474')
    passEntry.place(x=475, y=395)
    passEntry.config(show='*')
    Frame(register, width=230, height=2, bg='#81B9CB').place(x=475, y=415)

    confirmPassEntry = Entry(register, width=24, font=('Arial Rounded MT Bold', 12), bd=0, bg='#C2C1C1', fg='#747474')
    confirmPassEntry.place(x=475, y=445)
    confirmPassEntry.config(show='*')
    Frame(register, width=230, height=2, bg='#81B9CB').place(x=475, y=465)

    # Submit Button
    submitButton = Button(register, width=20, text='Submit', font=('Arial Rounded MT Bold', 12), bg='#12D0C5', activebackground='#12D0C5', fg='#000000', activeforeground='#000000', cursor='hand2')
    submitButton.place(x=485, y=490)

    # Already Have an Account Button
    registerButton = Button(register, width=25, text='Already Have an Account ?', font=('Arial Rounded MT Bold', 10), bd=0, bg='#C2C1C1', activebackground='#C2C1C1', fg='#000000', activeforeground='#000000', cursor='hand2',command=open_login)
    registerButton.place(x=490, y=530)

    # Eye Button for Password and Confirm Password Visibility Toggle
    hidePass = PhotoImage(file='Image/hide.png')
    eye_button = Button(register, image=hidePass, bd=0, bg='#C2C1C1', cursor='hand2', command=view_pass)
    eye_button.place(x=670, y=385)

    hidePass2 = PhotoImage(file='Image/hide.png')
    eye_button2 = Button(register, image=hidePass2, bd=0, bg='#C2C1C1', cursor='hand2', command=view_pass2)
    eye_button2.place(x=670, y=435)


        # Start the Registration Window
    register.mainloop()

# Test the function by calling it to show the register window
