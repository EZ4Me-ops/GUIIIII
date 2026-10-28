from tkinter import *

window=Tk()

username=Label(window,text="username",background="white")
username.place(x=250,y=250)

usernmaetype=Entry(window,background="red")
usernmaetype.place(x=350,y=250)


password=Label(window,text="password",background="white")
password.place(x=250,y=350)

passwordtype=Entry(window,background="red",show="*")
passwordtype.place(x=350,y=350)

btn1=Button(window,text="login",background="white")

btn2=Button(window,text="cancel",background="white")

btn1.place(x=250,y=400)

btn2.place(x=350,y=400)
window.mainloop()