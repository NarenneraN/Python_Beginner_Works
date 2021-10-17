from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

password_list = []

for char in range(nr_letters):
  password_list.append(random.choice(letters))

for char in range(nr_symbols):
  password_list += random.choice(symbols)

for char in range(nr_numbers):
  password_list += random.choice(numbers)

random.shuffle(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_info():
    web_name=website_entry.get()
    username=username_entry.get()
    password=password_entry.get()
    if len(web_name)==0 or len(username)==0 or len(password)==0:
        messagebox.showinfo(title="Error!",message="Please don't leave anny fields empty 🙄")
    else:
        cnfrm = messagebox.askokcancel(title="Confirmation",message=f"Details Entered :- \nEmail or UserName : {username}\nPassword : {password}\n"
                                                                  f"Website : {web_name}\nIs it ok to save")
        if cnfrm:
            with open("my_information.txt", "a") as info_file:
                info_file.write(f"{web_name} || {username} || {password}\n")
            website_entry.delete(0, END)
            username_entry.delete(0, END)
            password_entry.delete(0, END)
            website_entry.focus()



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

label_website = Label(text="Website:")
label_website.grid(row=1, column=0)
label_email_username = Label(text="Email/Username:")
label_email_username.grid(row=2, column=0)
label_password = Label(text="Password:")
label_password.grid(row=3, column=0)

website_entry = Entry()
website_entry.config(width=52)
website_entry.grid(column=1, row=1, columnspan=2)

username_entry = Entry()
username_entry.config(width=52)
username_entry.grid(column=1, row=2, columnspan=2)

password_entry = Entry()
password_entry.config(width=33)
password_entry.grid(column=1, row=3)

generate_button = Button(text="Generate Password")
generate_button.grid(column=2, row=3)

add_button = Button(text="Add",command=add_info)
add_button.config(width=44)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()