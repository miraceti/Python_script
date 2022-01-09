import tkinter as tk
from tkinter.constants import END


def updatelabel():
    label2.config(text=entry.get())
    # label2.config(text=label2.cget('text')+h)
    entry.delete('0',END)

root = tk.Tk()
root.title("stringvar")
root.geometry("300x150")

v = tk.StringVar()

entry = tk.Entry(root, textvariable = v) 
entry.place(x=80, y=40)

label = tk.Label(root, textvariable = v)
label.place(x=80, y=80)

v.set("Hellooo!")

h = v.get()

button2 = tk.Button(root, text="click", command=updatelabel) #version avec fonction classique
# button2 = tk.Button(root, text="click", command= lambda: label2.config(text=entry.get()) )#version directe avec lambda
button2.place (x=200, y=40)

label2 = tk.Label(root, text='vide')
label2.place(x=250, y=40)


root.mainloop()
