from tkinter import *

window=Tk()

window.geometry("100x100")

btn1=Button(window,text="exit application",background="red",command=window.destroy)
btn1.pack(side=LEFT)
window.mainloop()