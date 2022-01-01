from tkinter import *

window = Tk()

def submit():
    username = entry.get()
    print("Hello "+ username)
    entry.config()
    
def delete():
    entry.delete(0, END)
    
def backspace():
    entry.delete(len(entry.get())-1,END)
    


entry = Entry(window, font=("arial",50), fg="#00ff00", bg="black")
entry.insert(0, "test eponge")
entry.pack(side=LEFT)


submit_button = Button(window, text="submit", command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window, text="delete", command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window, text="backspace", command=backspace)
backspace_button.pack(side=RIGHT)


window.mainloop()