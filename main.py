import tkinter as tk
from tkinter import filedialog,messagebox
import random
import os

def hide_text(event=None):
    mainwindow.config(fg="#f7f5f5")
def character_count_update(event):
    content=mainwindow.get("1.0", tk.END)
    c=len(content)-1
    char_count_label.config(text=f"Character Count : {c}")
def save_file(event=None):
    download_path = os.path.expanduser("~/Downloads")
    base_file_name = "secret_note"
    file_extension = ".txt"
    file_index = 1
    file_name = f"{base_file_name}{file_index}{file_extension}"
    file_path = os.path.join(download_path, file_name)
    while os.path.exists(file_path):
        file_index += 1
        file_name = f"{base_file_name}{file_index}{file_extension}"
        file_path = os.path.join(download_path, file_name)
    
    with open(file_path, 'w') as file:
<<<<<<< HEAD
        download_path = os.path.expanduser("~\Documents")
        file_path = os.path.join(download_path, file_name)
=======
>>>>>>> ab05d485ccc4479c535dab2bf50a83a2820464ec
        content = random.choice(fake_data)
        file.write(content)
        print("File saved")
    messagebox.showinfo("Secret saved", f"Your secret has been saved to:\n{file_path}")

fake_data = ["Your secrets are safe... because they're not saved.",
"Secrets are meant to be forgotten!",
"Don't waste your time with secrets.",
"Lost in the void... just like your secrets.",
"No one will find this because it's never saved!",
"A memory is fleeting, just like this note.",
"Hidden so well, even you won't retrieve it.",
"Don't worry; your secrets are safe in the ether.",
"Shhh... it's a secret, or was it?",
"Like a whisper in the wind, this will be forgotten."
]
initial_message ="Type your secrets here..."
root = tk.Tk()
root.title("Secret Notepad with Encryption")
root.geometry("600x600")
root.configure(bg="#c4c4c4")

mainwindow = tk.Text(root, width=80, height=15,font=("Verdana" ,20), wrap="word",fg="#000000", bg="#f7f5f5", insertbackground="black")

mainwindow.pack(pady=10, padx=10)
mainwindow.insert("1.0", initial_message)

def on_focus_in(event):
    if mainwindow.get("1.0", tk.END).strip() == initial_message:
        mainwindow.delete("1.0", tk.END)
        mainwindow.config(fg="black")

def on_focus_out(event):
    if mainwindow.get("1.0", tk.END).strip() == "":
        mainwindow.insert("1.0", initial_message)
        mainwindow.config(fg="gray")

mainwindow.bind("<FocusIn>", on_focus_in)
mainwindow.bind("<FocusOut>", on_focus_out)

save_button=tk.Button(root , text="Save the secret message with Encryption",font=("Verdana",12), command=save_file)
save_button.pack(pady=10)

def on_text_change(event):
    mainwindow.config(fg="black")
    root.after(50, hide_text)

char_count_label = tk.Label(root, text="Character Count : 0", font=("Verdana",12),bg="#c4c4c4")
char_count_label.pack(pady=(5,10))

mainwindow.bind("<KeyRelease>", lambda event:[ on_text_change(event),character_count_update(event)])

root.mainloop()