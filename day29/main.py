from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [choice(letters) for letter in range(randint(8, 10))]

    password_list += [choice(symbols) for symbol in range(randint(2, 4))]

    password_list += [choice(numbers) for num in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)

    pass_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    # There is a website, a email/user, and pass
    website = website_entry.get()
    user = user_entry.get()
    password = pass_entry.get()

    # If a field is empty
    if len(website) == 0 or len(password) == 0 or len(user) == 0:
        messagebox.showerror(title="Oops", message="Please don't have any fields empty!")
        return
    
    # Checks if all info is valid according to user
    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail {user}\nPassword: {password} \nIs it ok to save?")

    if is_ok:
        with open("data.txt", mode="a+") as data:
            data.write(f"{website} | {user} | {password}\n")
        website_entry.delete(0, END)
        pass_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website: ")
website_label.grid(row=1, column=0)

user_label = Label(text="Email/Username: ")
user_label.grid(row=2, column=0)

pass_label = Label(text="Password: ")
pass_label.grid(row=3, column=0)

# Entry fields
website_entry = Entry()
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
website_entry.focus()

user_entry = Entry()
user_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
user_entry.insert(0, "email@domain.com")

pass_entry = Entry()
pass_entry.grid(row=3, column=1, sticky="EW")

# Buttons
generate_pass = Button(text="Generate Password", command=generate_password)
generate_pass.grid(row=3, column=2, sticky="EW")

add_button = Button(text="Add", width=36, command=add)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")
window.mainloop()