import json
import pyperclip
from random import *
from tkinter import *
from tkinter import messagebox


def generate_password():
    all_letters = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g',
                   'H', 'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n',
                   'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u',
                   'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z']
    all_symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    all_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    random_nums = [choice(all_numbers) for _ in range(randint(2, 5))]
    random_symb = [choice(all_symbols) for _ in range(randint(2, 5))]
    random_lets = [choice(all_letters) for _ in range(randint(5, 10))]

    password_list = random_lets + random_symb + random_nums
    shuffle(password_list)
    password = "".join(password_list)

    password_input.insert(0, password)
    pyperclip.copy(password)


def save_data():
    website = web_input.get()
    mail = mail_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": mail,
            "password": password,
        }
    }

    if len(website) == 0 or len(mail) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        try:
            with open("saved_notes.json", "r") as saved_notes:
                data = json.load(saved_notes)
        except FileNotFoundError:
            with open("saved_notes.json", "w") as saved_notes:
                json.dump(new_data, saved_notes, indent=4)
        else:
            data.update(new_data)

            with open("saved_notes.json", "w") as saved_notes:
                json.dump(data, saved_notes, indent=4)

        finally:
            web_input.delete(0, "end")
            mail_input.delete(0, "end")
            password_input.delete(0, "end")
            web_input.focus()


def search_info():
    website = web_input.get()
    try:
        with open("saved_notes.json", "r") as saved_notes:
            data = json.load(saved_notes)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="No data found")
    else:
        if website in data:
            mail = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=f"{website}", message=f"Mail/username: {mail}, \nPassword: {password}")
        else:
            messagebox.showinfo(title="Oops.", message=f"There's no info for {website}")


window = Tk()
window.title("Password Manager")
window.config(padx=25, pady=25)

canvas = Canvas(width=200, height=200)
app_logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=app_logo)
canvas.grid(column=1, row=0)

web_l = Label(text="Website:")
web_l.grid(column=0, row=1)
mail_username = Label(text="Mail/Username:")
mail_username.grid(column=0, row=2)
password_l = Label(text="Password:")
password_l.grid(column=0, row=3)

web_input = Entry(width=33)
web_input.focus()
web_input.grid(column=1, row=1)
mail_input = Entry(width=53)
mail_input.grid(column=1, row=2, columnspan=2)
password_input = Entry(width=33)
password_input.grid(column=1, row=3)

password_generator = Button(text="Generate password", width=15, command=generate_password)
password_generator.grid(column=2, row=3)
save_all = Button(text="Save to notes", width=44, command=save_data)
save_all.grid(row=4, column=1, columnspan=2)
search_button = Button(text="Search", width=15, command=search_info)
search_button.grid(column=2, row=1)

window.mainloop()
