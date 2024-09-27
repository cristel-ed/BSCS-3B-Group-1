from multiprocessing.resource_tracker import register
from shutil import which
from tkinter import *
from PIL import ImageTk



login= Tk()
login.geometry('900x660+200+15')
login.resizable(0,0)
login.title('Login Page')
bgImage = ImageTk.PhotoImage(file = 'image/LoginForm.jpg')
bg_label =Label(login,image=bgImage)
bg_label.place(x=0,y=0)

def view_pass():
    hidepass.config(file='image/view.png')
    passEntry.config(show='')
    eye_button.config(command=hide_pass)

def hide_pass():
    hidepass.config(file='image/hide.png')
    passEntry.config(show='*')
    eye_button.config(command=view_pass)

def use_enter(event):
    if userEntry.get()=='username':
        userEntry.delete(0,END)

def use_pass(event):
    if passEntry.get() == 'password':
        passEntry.config(show='*')
        passEntry.delete(0, END)


heading=Label(login,text='Evaluation System',font=('Arial Rounded MT Bold',23,'bold'),bg='#DCDBDB',fg='#747474')
heading.place(x=445,y=120)
heading=Label(login,text='Login Form',font=('Arial Rounded MT Bold',15),bg='#DCDBDB',fg='#747474')
heading.place(x=530,y=170)
heading=Label(login,text='Username',font=('Arial Rounded MT Bold',15),bg='#DCDBDB',fg='#747474')
heading.place(x=430,y=270)
heading=Label(login,text='Password',font=('Arial Rounded MT Bold',15),bg='#DCDBDB',fg='#747474')
heading.place(x=430,y=350)


userEntry=Entry(login,width=23,font=('Arial Rounded MT Bold',12),bd=0,bg='#DCDBDB',fg='#12D0C5')
userEntry.place(x=440,y=310)
userEntry.insert(0,'username')
userEntry.bind('<FocusIn>',use_enter)
Frame(login,width=285,height=2,bg='#50D7CF').place(x=440,y=335)

passEntry=Entry(login,width=24,font=('Arial Rounded MT Bold',12),bd=0,bg='#DCDBDB',fg='#12D0C5')
passEntry.place(x=440,y=390)
passEntry.insert(0,'password')
passEntry.bind('<FocusIn>',use_pass)
Frame(login,width=285,height=2,bg='#50D7CF').place(x=440,y=415)

hidepass=PhotoImage(file = 'image/hide.png')
eye_button=Button(login,image=hidepass,bd=0,bg='#DCDBDB',cursor='hand2',command=view_pass)
eye_button.place(x=690,y=380)

loginButton=Button(login,width=20,text='Submit',font=('Arial Rounded MT Bold',12),bg='#12D0C5',activebackground='#12D0C5',fg='#DCDBDB',activeforeground='#DCDBDB',cursor='hand2')
loginButton.place(x=475,y=450)

registerButton=Button(login,width=15,text='Create an Account',font=('Arial Rounded MT Bold',10),bd=0,bg='#DCDBDB',activebackground='#DCDBDB',fg='#12D0C5',activeforeground='#12D0C5',cursor='hand2')
registerButton.place(x=520,y=500)


login.mainloop()