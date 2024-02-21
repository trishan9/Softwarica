from tkinter import Button, Entry, Label, Tk

window = Tk()
window.title("Tkinter")
# window.geometry("1920x1080")
window.minsize(width=1920, height=1000)
window.maxsize(width=1920, height=1000)
window.config(pady=16, padx=16)

our_text = 0


def increment():
    global our_text
    our_text += 1
    text_label.config(text=our_text)


def decrement():
    global our_text
    if our_text == 0:
        return text_label.config(text="0")
    our_text -= 1
    text_label.config(text=our_text)


def save_name():
    name_label.config(text=name_input.get())


plus_button = Button(
    text="+", font=("Arial", 36, "bold"), fg="#1b1b1b", command=increment
)
text_label = Label(text=our_text, font=("Arial", 36, "bold"), fg="#1b1b1b")
minus_button = Button(
    text="-", font=("Arial", 36, "bold"), fg="#1b1b1b", padx=18, command=decrement
)
name_input = Entry()
save_button = Button(text="Save Changes", command=save_name)
name_label = Label(text="Your Name Goes Here....")

plus_button.grid(row=0, column=0)
text_label.grid(row=0, column=1)
minus_button.grid(row=0, column=2)
name_input.grid(row=1, column=3)
save_button.grid(row=1, column=4)
name_label.grid(row=2, column=5)

window.mainloop()
