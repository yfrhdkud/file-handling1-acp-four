from tkinter import *
from random import *
       
characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"


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
window.title("Tkinter Sample Window")
window.geometry("300x150")

label = Label(text ="Random Password generator", fg = "black", bg = "white", height=3, width=100)

button = Button(text = "Click me" , bg = "black" , fg = "white" ,height=2, width=10, command=generate)
button_copy = Button(text="Copy", bg="green", fg="white", height=2, width=10, command=copyC)
entry = Entry(fg = "yellow" , bg = "blue", width=50, justify="center")

label.pack()
button.pack()
entry.pack()
button_copy.pack(pady=5)

window.mainloop()

