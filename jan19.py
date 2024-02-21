from tkinter import *

root = Tk()
root.geometry("780x780")
root.title("January 19")


def on_click():
    value = input.get()
    input.delete(0, END)
    text.config(text=value)


text = Label(text="")
text.pack()

btn = Button(text="Click Me", command=lambda: on_click())
btn.pack()

input = Entry()
input.pack()

root.mainloop()
