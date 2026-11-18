from tkinter import *

window = Tk()
window.title("CALENDAR")
# window.geometry()
window.config(bg="white")

top=Frame(window)
top.pack()

def convert():
    poundss=float(enter.get())*2.20462
    gramss=float(enter.get())*1000
    ouncess=float(enter.get())*35.274

    
    gramnum.config(text=gramss)
    poundsnum.config(text=poundss)
    ouncenum.config(text=ouncess)


text=Label(top,text="weight in kg")
text.grid(row=0,column=0)

enter=Entry(top,text="weight in kg")
enter.grid(row=0,column=1)

but=Button(top,text="convert",command=convert)
but.grid(row=0,column=2)

bottom=Frame(window)
bottom.pack()


gram=Label(bottom,text="gram")
gram.grid(row=0,column=0,padx=15)

pounds=Label(bottom,text="pounds")
pounds.grid(row=0,column=1,padx=15)

ounce=Label(bottom,text="ounce")
ounce.grid(row=0,column=2,padx=15)



gramnum=Label(bottom,)
gramnum.grid(row=1,column=0,padx=15)

poundsnum=Label(bottom,)
poundsnum.grid(row=1,column=1,padx=15)

ouncenum=Label(bottom,)
ouncenum.grid(row=1,column=2,padx=15)



window.mainloop()
