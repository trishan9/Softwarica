from tkinter import Tk, Label, Entry, Button
from PIL import ImageTk, Image

root = Tk()
root.config(padx=40, pady=50, bg="#f5f5f5")
root.title("Login Page")

my_image = ImageTk.PhotoImage(Image.open("./vidyarthi.png"), width=48, height=48)


def register_page():
    root.destroy()
    import register


heading = Label(text="Login Page", font=("Arial", 18, "bold"), bg="#f5f5f5")
heading.grid(row=0, column=0, columnspan=2, pady=8)

email_label = Label(text="Email", bg="#f5f5f5")
email_label.grid(row=1, column=0)

email_input = Entry(bg="#f5f5f5")
email_input.grid(row=1, column=1)

password_label = Label(text="Password", bg="#f5f5f5")
password_label.grid(row=2, column=0, pady=4)

password_input = Entry(bg="#f5f5f5")
password_input.grid(row=2, column=1, pady=4)

submit_button = Button(text="Login", width=17, bg="#ffffff")
submit_button.grid(row=3, column=1, columnspan=2, pady=6)

back_button = Button(
    text="Go to register page", width=17, bg="#ffffff", command=register_page
)
back_button.grid(
    row=4,
    column=1,
    columnspan=2,
    pady=6,
)
image_label = Label(image=my_image)
image_label.grid(row=4, column=0)


root.mainloop()
