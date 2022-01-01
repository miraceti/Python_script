from tkinter import *


def openfile():
    print("file has been opened")
    
def savefile():
    print("file has been saved")    

def cut():
    print("you cut some text")

def copy():
    print("you copy some text")

def paste():
    print("you paste some text")

window = Tk()

menubar = Menu(window)
window.config(menu=menubar)

filemenu = Menu(menubar, tearoff=0, font=("MV Boli",15))
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Open", command=openfile)
filemenu.add_command(label="Save", command=savefile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=quit)

editmenu = Menu(menubar, tearoff=0, font=("MV Boli",15))
menubar.add_cascade(label="Edit", menu=editmenu)
editmenu.add_command(label="Cut", command=cut)
editmenu.add_command(label="Copy", command=copy)
editmenu.add_command(label="Paste", command=paste)

frame = Frame(window, bg="pink", bd=5, relief=RAISED)
frame.pack(side=BOTTOM)

Button(frame, text="W", font=("Consolas", 25), width=0).pack(side=TOP)
Button(frame, text="A", font=("Consolas", 25), width=0).pack(side=LEFT)
Button(frame, text="S", font=("Consolas", 25), width=0).pack(side=LEFT)
Button(frame, text="D", font=("Consolas", 25), width=0).pack(side=LEFT)

def create_window():
    new_window = Tk() #or TopLevel()
    # new_window = Toplevel()
    window.destroy() #destruction de la fenêtre initiale

# new window
button = Button(window, text="create new window", command=create_window).pack()

window.mainloop()