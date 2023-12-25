# Description: A flash card app that helps you learn new languages
# After 3 seconds, the card will flip to show the translation
# If you know the word, click the check button and the word will be removed from the list
# If you don't know the word, click the x button and the word will be shown again in the future

from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}
current_card = {}

try: 
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError: 
    original_data = pandas.read_csv("data/data.csv")
    to_learn = original_data.to_dict(orient="records")
else: 
    to_learn = data.to_dict(orient="records")


def new_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["french"])
    canvas.itemconfig(card_bg, image=card_front_img)
    # after 3 seconds, flip the card
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["english"])
    canvas.itemconfig(card_bg, image=card_back_img)


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    new_card()

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# after 3 seconds, flip the card
flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_bg = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=new_card)
wrong_button.grid(row=1, column=0)

check_img = PhotoImage(file="images/correct.png")
check_button = Button(image=check_img, highlightthickness=0, command=is_known)
check_button.grid(row=1, column=1)


new_card()

window.mainloop()