import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("USD ⇄ INR Currency Converter")
root.geometry("360x280")
root.resizable(False, False)
root.configure(padx=20, pady=20)

title_label = tk.Label(root, text="Currency Converter", font=("Arial", 16, "bold"))
title_label.pack(pady=(0, 10))

root.mainloop()