from tkinter import *

def submit():
    print("the temperature is " + str(scale.get()) + " degrees Celcius")


window = Tk()

hotImage = PhotoImage(file="hotdog.png")
hotLabel = Label(image=hotImage)
hotLabel.pack()


scale = Scale(window, from_=100, to=0,
              length=300, orient =VERTICAL,
              font=("Consolas",20),
              tickinterval = 10,#add numerics indicator 
            #   showvalue = 0,#hide current value
              resolution=5 ,#increment of slider
              troughcolor= 'blue',
              fg='#ff1c00',
              bg='#111111'
              )
# scale.set(50)
scale.set(((scale['from']-scale['to'])/2) + scale['to'])

scale.pack()
coldImage = PhotoImage(file="cold.png")
coldLabel = Label(image=coldImage)
coldLabel.pack()
button = Button(window, text="submit", command = submit)
button.pack()

window.mainloop()