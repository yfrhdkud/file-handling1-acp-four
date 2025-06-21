from tkinter import *
from random import *

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"

# hopefully this works
def generate():
    length = randint(8, 16)
    password = ''.join(choice(characters) for _ in range(length))
    entry.delete(0, END)
    entry.insert(0, password)

def copyC():
    password = entry.get()
    window.clipboard_clear()
    window.clipboard_append(password)

window = Tk()
window.title("Random Password Generator")
window.geometry("400x300")
window.configure(bg="#f0f0f0") 

title_label = Label(
    window,
    text="Random Password Generator",
    font=("Helvetica", 14, "bold"),
    bg="#f0f0f0",
    fg="#333"
)
title_label.pack(pady=10)

entry = Entry(window, font=(14), fg="#222", bg="#e0e0e0", width=28, justify="center", relief=FLAT)
entry.pack(pady=10, ipady=5)

button = Frame(window, bg="#f0f0f0")
button.pack(pady=20)

generate_button = Button(button, text="Generate", font=("Arial", 10), bg="#4CAF50", fg="white", width=12, command=generate)
copy_button = Button(button, text="Copy", font=("Arial", 10), bg="#2196F3", fg="white", width=12, command=copyC)

generate_button.grid(row=0, column=0, padx=10)
copy_button.grid(row=0, column=1, padx=10)

window.mainloop()
