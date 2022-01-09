import tkinter as tk
from PIL import Image, ImageTk

root =tk.Tk()
root.title("resize image in label")
root.geometry("300x150")

#1rst approach
photo = tk.PhotoImage(file="mando2.png")

#2nd approach
photo2 = Image.open("mando2.png")
resized_image = photo2.resize((300,150), Image.ANTIALIAS)
converted_image = ImageTk.PhotoImage(resized_image)

label = tk.Label(root, image= photo2, width=300, height=150, bg='black', fg='yellow' )
label.pack()

root.mainloop()
