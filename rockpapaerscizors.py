from tkinter import *
from tkinter import messagebox

screen=Tk()
screen.geometry("760x390")
screen.config(bg="#000080")

title=Label(screen,fg="#8c8c8c",text="wecome to rock papaer and sissor hwhwhwhwh",font=(12))
title.grid(row=0,column=0,padx=10,columnspan=3)

bt1=Button(screen,text="Rock",bg="#8c8c8c")
bt1.grid(row=1,column=0,padx=24)

bt2=Button(screen,text="paper",bg="#8c8c8c")
bt2.grid(row=1,column=1,padx=24)

bt3=Button(screen,text="sizor",bg="#8c8c8c")
bt3.grid(row=1,column=2,padx=24)
screen.mainloop()
