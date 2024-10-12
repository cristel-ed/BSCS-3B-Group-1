from tkinter import *
from PIL import ImageTk
import functions

def open_registerform():
    register = Tk()
    register.geometry('1024x720+180+0')
    register.overrideredirect(True)
    register.title('Register Page')

    backgroundImage = PhotoImage(file='Image/Signup.png')
    bg_label = Label(register, image=backgroundImage)
    bg_label.place(x=0, y=0)

    # Entry Fields
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
    passEntry = Entry(register, width=25, font=('Arial Rounded MT Bold', 20), bd=0, bg='#ADD1FB', fg='#000000', show='*')
    passEntry.place(x=521, y=499)
    cpassEntry = Entry(register, width=25, font=('Arial Rounded MT Bold', 20), bd=0, bg='#ADD1FB', fg='#000000', show='*')
    cpassEntry.place(x=521, y=584)

    # Password Toggle Buttons
    hidePass = PhotoImage(file='Image/hide.png')
    eye_button = Button(
        register, image=hidePass, bd=0, bg='#ADD1FB', activebackground='#ADD1FB',
        cursor='hand2', command=lambda: functions.view_pass(passEntry, eye_button, hidePass)
    )
    eye_button.place(x=910, y=503)

    hidePass2 = PhotoImage(file='Image/hide.png')
    eye_button2 = Button(
        register, image=hidePass2, bd=0, bg='#ADD1FB', activebackground='#ADD1FB',
        cursor='hand2', command=lambda: functions.view_pass(cpassEntry, eye_button2, hidePass2)
    )
    eye_button2.place(x=910, y=587)

    # Buttons
    registerButton = Button(
        register, width=10, text='Submit', font=('Arial Rounded MT Bold', 14), bd=0,
        bg='#ADD1FB', activebackground='#ADD1FB', cursor='hand2',
        command=lambda: functions.register_user(
            fNameEntry, lNameEntry, studentIDEntry, courseEntry, yearnsecEntry,
            userEntry, passEntry, cpassEntry, register
        )
    )
    registerButton.place(x=665, y=641)

    signupButton = Button(
        register, width=5, text='Sign in', font=('Arial Rounded MT Bold', 12), bd=0,
        bg='#ffffff', activebackground='#ffffff', fg='#50C2C9', activeforeground='#50C2C9',
        cursor='hand2', command=lambda: functions.open_login(register)
    )
    signupButton.place(x=810, y=689)

    xImage = PhotoImage(file='Image/X-ICon.png')
    close_button = Button(
        register, image=xImage, command=lambda: functions.close_window(register),
        bg='#FBADAD', fg='#000000', activebackground='#FBADAD', font=('Arial', 10),
        bd=0, cursor='hand2'
    )
    close_button.place(x=973, y=22)
    register.bind('<Return>', lambda event: functions.register_user(fNameEntry, lNameEntry, studentIDEntry, courseEntry,
    yearnsecEntry, userEntry, passEntry, cpassEntry, register))
    register.mainloop()
