from tkinter import END, Tk, Entry, Label, Button, Text
from tkinter import messagebox

root = Tk()
root.geometry("750x750")


def submit_details():
    print(message_box.get("1.0", END))
    fname = fname_input.get()
    lname = lname_input.get()
    gender = gender_input.get()
    age = age_input.get()

    if fname and lname and gender and age:
        user_details = f"Name: {fname} {lname}\nGender: {gender}\nAge: {age}"
        confirm = messagebox.askyesno(title="Confirm Details", message=user_details)
        if confirm:
            details.config(text=user_details)
    else:
        messagebox.showerror(title="Error", message="All the fields are required!")


fname_label = Label(text="First Name")
fname_input = Entry()

lname_label = Label(text="Last Name")
lname_input = Entry()

gender_label = Label(text="Gender")
gender_input = Entry()

age_label = Label(text="Age")
age_input = Entry()

message_label = Label(text="Message")
message_box = Text(width=80, height=5)


submit_button = Button(text="Submit", command=submit_details)

details = Label(text="")
details.grid(row=6, column=0)

fname_label.grid(row=0, column=0)
fname_input.grid(row=0, column=1)
lname_label.grid(row=1, column=0)
lname_input.grid(row=1, column=1)
gender_label.grid(row=2, column=0)
gender_input.grid(row=2, column=1)
age_label.grid(row=3, column=0)
age_input.grid(row=3, column=1)
message_label.grid(row=4, column=0)
message_box.grid(row=4, column=1)
submit_button.grid(row=5, column=0, columnspan=2)


root.mainloop()
