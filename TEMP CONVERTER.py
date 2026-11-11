
from tkinter import *

# Create the main window
window = Tk()
window.title("Temperature Converter")
window.geometry("350x300")
window.config(bg="white")

# Function to convert temperature
def convert():
    celsius = float(entry.get())
    fahrenheit = (celsius * 9/5) + 32

    result.config(text="Temperature in Fahrenheit: " + str(round(fahrenheit, 1)))

# Create the title
title = Label(window, text="Celsius -> Fahrenheit",
              font=("Arial", 18), bg="white")
title.pack(pady=15)

# Create the label
label = Label(window, text="Enter Temperature in Celsius:",
              bg="white")
label.pack(pady=5)

# Create the entry box
entry = Entry(window)
entry.pack(pady=5)

# Create the result label
result = Label(window, text="", font=("Arial", 11), bg="white")
result.pack(pady=10)

# Create the convert button
button = Button(window, text="Convert",
                command=convert, bg="lightgreen",
                width=20)
button.pack(pady=15)

# Create the exit button
exitbutton = Button(window, text="Exit",
                    command=window.destroy)
exitbutton.pack()

# Run the window
window.mainloop()
