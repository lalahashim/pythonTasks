from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
LANG_FONT = "Ariel", 30, "italic"
WORD_FONT = "Ariel", 40, "bold"

current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=front_color)
    flip_timer = window.after(5000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=back_color)


def is_known():
    to_learn.remove(current_card)
    known_words = pandas.DataFrame(to_learn)
    known_words.to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title('Flash cards')
window.config(padx=50, pady=50)
window.config(bg=BACKGROUND_COLOR)

flip_timer = window.after(5000, func=flip_card)

canvas = Canvas(width=800, height=525, highlightthickness=0, bg=BACKGROUND_COLOR)
front_color = PhotoImage(file="images/card_front.png")
back_color = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 268, image=front_color)
card_title = canvas.create_text(400, 150, text="Title", fill="black", font=LANG_FONT)
card_word = canvas.create_text(400, 263, text="word", fill="black", font=WORD_FONT)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
cross_b = Button(image=cross_image, highlightthickness=0, command=next_card)
cross_b.grid(row=1, column=0)

tick_image = PhotoImage(file="images/right.png")
tick_b = Button(image=tick_image, highlightthickness=0, command=is_known)
tick_b.grid(row=1, column=1)

window.mainloop()
