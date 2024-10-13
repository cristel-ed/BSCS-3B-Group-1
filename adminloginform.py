#adminloginform.py
from tkinter import *
from functions import user_auth
from functions import navigation
from functions import password_visibility


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

    userEntry = Entry(admin, width=19, font=('Arial Rounded MT Bold', 20), bd=0, bg='#ADD1FB', fg='#000000')
    userEntry.place(x=568, y=316)

    passEntry = Entry(admin, width=19, font=('Arial Rounded MT Bold', 20), bd=0, bg='#ADD1FB', fg='#000000', show='*')
    passEntry.place(x=568, y=435)

    # Corrected button command to use a lambda function
    adminButton = Button(admin, width=8, text='Submit', font=('Arial Rounded MT Bold', 15), bd=0,
                         bg='#ADD1FB', activebackground='#ADD1FB', cursor='hand2',
                         command=lambda: user_auth.admin_user(userEntry, passEntry, admin))
    adminButton.place(x=666, y=520)

    signupButton = Button(admin, width=9, text='Login Here', font=('Arial Rounded MT Bold', 12), bd=0,
                          bg='#ffffff', activebackground='#ffffff', fg='#50C2C9',
                          activeforeground='#50C2C9', cursor='hand2',
                          command=lambda: navigation.open_login(admin))
    signupButton.place(x=765, y=594)

    hidePass = PhotoImage(file='Image/hide.png')
    eye_button3 = Button(admin, image=hidePass, bd=0, bg='#ADD1FB', activebackground='#ADD1FB',
                         cursor='hand2',
                         command=lambda: password_visibility.view_pass(passEntry, eye_button3, hidePass))
    eye_button3.place(x=885, y=440)

    # Use lambda function for event binding
    admin.bind('<Return>', lambda event: user_auth.admin_user(userEntry, passEntry, admin))

    # Create a custom close button (X)
    xImage = PhotoImage(file='Image/X-ICon.png')
    close_button = Button(admin, image=xImage, command=lambda: navigation.close_window(admin),
                          bg='#FBADAD', fg='#000000', activebackground='#FBADAD',
                          font=('Arial', 10), bd=0, cursor='hand2')
    close_button.place(x=973, y=22)

    admin.mainloop()
