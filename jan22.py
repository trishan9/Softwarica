from tkinter import BooleanVar, Button, Tk, Label, Radiobutton, StringVar, Checkbutton

root = Tk()
root.geometry("400x400")


def open_login_page():
    root.destroy()
    import login


gender_label = Label(text="")
gender_label.pack()

gender = StringVar()

male_radio = Radiobutton(
    text="Male",
    value="Male",
    variable=gender,
    command=lambda: gender_label.config(text=gender.get()),
)
male_radio.pack()

female_radio = Radiobutton(
    text="Female",
    value="Female",
    variable=gender,
    command=lambda: gender_label.config(text=gender.get()),
)
female_radio.pack()

hobby = Label(text="")
hobby.pack()


def save_hobbies():
    if isSports.get() and isMusic.get():
        hobby.config(text="Sports, Music")
    elif isSports.get():
        hobby.config(text="Sports")
    elif isMusic.get():
        hobby.config(text="Music")
    else:
        hobby.config(text="")


isMusic = BooleanVar()
music_checkbutton = Checkbutton(
    text="Music", variable=isMusic, onvalue=True, offvalue=False
)
music_checkbutton.pack()

isSports = BooleanVar()
sports_checkbutton = Checkbutton(
    text="Sports", variable=isSports, onvalue=True, offvalue=False
)
sports_checkbutton.pack()

save_button = Button(text="Save", command=save_hobbies)
save_button.pack()

login_button = Button(text="Open Login Page", command=open_login_page)
login_button.pack()

root.mainloop()
