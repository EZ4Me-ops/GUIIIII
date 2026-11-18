from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Temperature Converter")
window.geometry("350x300")
window.config(bg="white")

# messagebox.showinfo(title="gog",message="bubmbu")
# messagebox.showerror(title="asd",message="za")
# messagebox.showwarning(title="asd",message="za")
gog=messagebox.askquestion(title="fag",message="what is the meaning for gaag")
print(gog)

asd=messagebox.askokcancel(title="fag",message="whatasfdasdr gaag")
print(asd)

wasd=messagebox.askretrycancel(title="fag",message="asfasfd gaag")
print(wasd)

was12d=messagebox.askyesnocancel(title="fagasf",message="asfasdgg")
print(was12d)
window.mainloop()