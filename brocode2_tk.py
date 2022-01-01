from tkinter import *

window = Tk()

def submit():
    username = entry.get()
    print("Hello "+ username)
    # entry.config(state=DISABLED)
    
def delete():
    entry.delete(0, END)
    
def backspace():
    entry.delete(len(entry.get())-1,END)
    


entry = Entry(window, font=("arial",50), fg="#00ff00", bg="black", show="*")
# entry.insert(0, "test eponge")
entry.pack(side=LEFT)


submit_button = Button(window, text="submit", command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window, text="delete", command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window, text="backspace", command=backspace)
backspace_button.pack(side=RIGHT)

def display():
    if (x.get()==1):
        print("you agree")
    else:
        print("you don't agree")

# check 
x = IntVar()
python_photo = PhotoImage(file="pngegg.png")
check_button = Checkbutton(window, text="i agee to something", variable=x, onvalue=1, offvalue=0, 
                           command=display, font=("arial",20), fg="#00ff00", bg='black',
                           activeforeground = "#00ff00", activebackground="black",
                           padx=25, pady=10, 
                           image=python_photo, compound='left'
                           )
check_button.pack()

# radiobutton
def order ():
    if (x.get()== 0):
        print("you ordered a pizza")==1
    elif (x.get()==1):
        print("you ordered a hamburger")
    elif (x.get()==2):
        print("you ordered a hotdog")
    else:
        print("hu?")
        
food = ["pizza","hamburger","hotdog"]
x = IntVar()
pizzaimage = PhotoImage(file="pizza.png")
hamburgerimage = PhotoImage(file="hamburger.png")
hotdogimage = PhotoImage(file="hotdog.png")
foodimages =[pizzaimage,hamburgerimage,hotdogimage]
for index in range(len(food)):
    radiobutton = Radiobutton(window, text=food[index], variable=x, value=index, padx=25, font=("Impact",50),
                              image=foodimages[index], compound='left',
                              indicatoron = 0, width=375,
                              comman = order)
    radiobutton.pack(anchor=W)

window.mainloop()