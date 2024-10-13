#loginform.py
from tkinter import *
from functions import user_auth
from functions import navigation
from functions import password_visibility


def open_loginform():
    login = Tk()
    login.geometry('1024x720+180+0')
    login.overrideredirect(True)
    login.title('Login Page')

    backgroundImage = PhotoImage(file='Image/LoginPage.png')
    bg_label = Label(login, image=backgroundImage)
    bg_label.place(x=0, y=0)

    userEntry = Entry(login, width=19, font=('Arial Rounded MT Bold', 20), bd=0, bg='#ADD1FB', fg='#000000')
    userEntry.place(x=568, y=316)

    passEntry = Entry(login, width=19, font=('Arial Rounded MT Bold', 20), bd=0, bg='#ADD1FB', fg='#000000', show='*')
    passEntry.place(x=568, y=435)

    loginButton = Button(login, width=8, text='Submit', font=('Arial Rounded MT Bold', 15), bd=0, bg='#ADD1FB',
                         activebackground='#ADD1FB', cursor='hand2',
                         command=lambda: user_auth.login_user(userEntry, passEntry, login))
    loginButton.place(x=666, y=520)

    signupButton = Button(login, width=6, text='Sign up', font=('Arial Rounded MT Bold', 12), bd=0, bg='#ffffff',
                          activebackground='#ffffff', fg='#50C2C9', activeforeground='#50C2C9', cursor='hand2',
                          command=lambda: navigation.open_register(login))
    signupButton.place(x=795, y=594)

    adminImage = PhotoImage(file='Image/AdminButton.png')
    adminButton = Button(login, image=adminImage, bd=0, bg='#FBADAD', activebackground='#FBADAD', cursor='hand2',
                         command=lambda: navigation.open_admin(login))
    adminButton.place(x=900, y=630)

    hidePass = PhotoImage(file='Image/hide.png')
    eye_button = Button(login, image=hidePass, bd=0, bg='#ADD1FB', activebackground='#ADD1FB', cursor='hand2',
                        command=lambda: password_visibility.view_pass(passEntry, eye_button, hidePass))
    eye_button.place(x=885, y=440)

    xImage = PhotoImage(file='Image/X-ICon.png')
    close_button = Button(login, image=xImage, command=lambda: navigation.close_window(login), bg='#FBADAD', fg='#000000',
                          activebackground='#FBADAD', font=('Arial', 10), bd=0, cursor='hand2')
    close_button.place(x=973, y=22)

    login.bind('<Return>', lambda event: user_auth.login_user(userEntry, passEntry, login))
    login.mainloop()

if __name__ == '__main__':
    open_loginform()
