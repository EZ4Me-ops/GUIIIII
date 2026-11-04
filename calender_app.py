from tkinter import *
import calendar

# Create the main window
window = Tk()
window.title("CALENDAR")
window.geometry("330x300")
window.config(bg="white")

def show():
    cal=Tk()
    cal.title("CALENDAR")
    cal.config(bg="white")
    calen=Text(cal,height=50)
    calen.pack()
    year=int(yearentry.get())
    showcalendar=calendar.calendar(year)
    calen.insert(END,showcalendar)
    cal.mainloop()

title=Label(window,text="CALENDER",font=("Times New Roman",30))
title.pack(pady=15)

yearlabel=Label(window,text="enter year",font=("Arial",12))
yearlabel.pack(pady=15)

yearentry=Entry(window)
yearentry.pack()

btn1=Button(window,text="show calender",command=show)
btn1.pack(pady=10)

exit=Button(window,text="exit",command=exit)
exit.pack(pady=10)
window.mainloop()