import tkinter  as tk

root = tk.Tk()
root.title("entry_2_label_via_button")
root.geometry("300x150")


def get_value2():
    v = entry.get()
    button2.config(text = v)
    
def get_value():
    v = entry.get()
    label.config(text = v)
    
entry = tk.Entry(root)
entry.place(x = 10, y = 40)
entry.insert(0, "enter the username")

entry2 = tk.Entry(root, show="*")
entry2.place(x = 140, y = 40)
entry2.insert(0, "enter the username2")

label = tk.Label(root, text="empty label")
label.place(x = 80, y = 120)

button = tk.Button(root, text="process entry widget", command=get_value)
button.place(x = 10, y = 80)

button2 = tk.Button(root, text="process entry widget2", command=get_value2)
button2.place(x = 140, y = 80)

root.mainloop()