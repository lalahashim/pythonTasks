#password generater 
import random

all_letters = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 
               'H', 'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 
               'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 
               'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z']
all_symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
all_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to the PyPassword Generator!")

lets_num = int(input("How many letters would you like in your password?\n"))
symb_num = int(input("How many symbols would you like in your password?\n"))
numb_num = int(input("How many numbers would you like in your password?\n"))

password_list = []
for char in range(1, lets_num + 1):
    password_list.append(random.choice(all_letters))
for char in range(1, symb_num + 1):
    password_list += random.choice(all_symbols)
for char in range(1, numb_num + 1):
    password_list += random.choice(all_numbers)

random.shuffle(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")