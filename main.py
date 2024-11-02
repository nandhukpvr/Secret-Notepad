import tkinter as tk
import random

def hide_text(event=None):
    mainwindow.config(fg="#f7f5f5")


root = tk.Tk()
root.title("Secret Notepad with Encryption")
root.geometry("600x500")
root.configure(bg="#c4c4c4")

mainwindow = tk.Text(root, width=80, height=20,font=("Verdana" ,20), wrap="word",fg="#000000", bg="#f7f5f5", insertbackground="black")
mainwindow.pack(pady=10)

def on_text_change(event):
    mainwindow.config(fg="black")
    root.after(50, hide_text)

mainwindow.bind("<KeyRelease>", on_text_change)

root.mainloop()