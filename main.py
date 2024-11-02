import tkinter as tk
import random

def hide_text(event=None):
    mainwindow.config(fg="#f7f5f5")
def character_count_update(event):
    content=mainwindow.get("1.0", tk.END)
    c=len(content)-1
    char_count_label.config(text=f"Character Count : {c}")

root = tk.Tk()
root.title("Secret Notepad with Encryption")
root.geometry("600x600")
root.configure(bg="#c4c4c4")

mainwindow = tk.Text(root, width=80, height=15,font=("Verdana" ,20), wrap="word",fg="#000000", bg="#f7f5f5", insertbackground="black")
mainwindow.pack(pady=10, padx=10)


def on_text_change(event):
    mainwindow.config(fg="black")
    root.after(50, hide_text)

char_count_label = tk.Label(root, text="Character Count : 0", font=("Verdana",12),bg="#c4c4c4")
char_count_label.pack(pady=(5,10))

mainwindow.bind("<KeyRelease>", lambda event:[ on_text_change(event),character_count_update(event)])

root.mainloop()