from tkinter import *
import os
from tkinter import messagebox
import random
import pyperclip

# ------------------------------ PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "y", "z",
            "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "L", "K",
            "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "Y", "Z"]
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    # clear the password entry
    password_entry.delete(0, END)
    
    # generate random letters, numbers and symbols
    num_letters = random.randint(8, 10)
    num_numbers = random.randint(2, 4)
    num_symbols = random.randint(2, 4)

    pass_letters = [random.choice(letters) for _ in range(num_letters)]
    pass_numbers = [random.choice(numbers) for _ in range(num_numbers)]
    pass_symbols = [random.choice(symbols) for _ in range(num_symbols)]

    # join the lists and shuffle them
    password_list = pass_letters + pass_numbers + pass_symbols
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)

    # copy the password to the clipboard
    pyperclip.copy(password)


# ------------------------------ SAVE PASSWORD ------------------------------- #


def save_password():
    # get the entries
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # check if the entries are empty
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        # Ask the user if the information is correct
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}\nPassword: {password}\nIs it ok to save?")

        if is_ok:
            # delete the entries
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)

            # if the file does not exist, create the file pass_manager.csv and save the data
            # if the file exists, append the data to the file
            if not os.path.exists("pass_manager.csv"):
                with open("pass_manager.csv", "w") as file:
                    file.write("website,email,password\n")
                    file.write(f"{website},{email},{password}\n")
            else:
                with open("pass_manager.csv", "a") as file:
                    file.write(f"{website},{email},{password}\n")

            # refocus the cursor on the website entry
            website_entry.focus()



# ------------------------------ UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, background="#fff")


canvas = Canvas(width=200, height=200, background="#fff", highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=0, columnspan=3)


website_label = Label(text="Website:", background="#fff", pady=10)
website_label.grid(row=1, column=0, padx=(0,25))
website_entry = Entry(width=40)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)

email_label = Label(text="Email/Username:", background="#fff", pady=10)
email_label.grid(row=2, column=0, padx=(0,25))
email_entry = Entry(width=40)
email_entry.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password:", background="#fff", pady=10)
password_label.grid(row=3, column=0, padx=(0,25))
password_entry = Entry(width=20)
password_entry.grid(row=3, column=1)
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=33, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()