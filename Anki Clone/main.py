from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
card = None
flipping = None

# csv reading
try:
    data = pd.read_csv("./data/to_learn.csv").to_dict(orient="records")
except FileNotFoundError:
    data = pd.read_csv("./data/french_words.csv").to_dict(orient="records")

# Window config
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
# window.minsize(1000, 1000)

# Functions
def gen_word_fr(check):
    global card, flipping
    if flipping is not None:
        window.after_cancel(id=flipping)
    
    if check == True:
        data.remove(card)
        to_learn = pd.DataFrame(data)
        to_learn.to_csv("./data/to_learn.csv", index=False)

    card = random.choice(data)
    fr_word = card['French']

    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word_label, text=fr_word, fill="black")
    canvas.itemconfig(img, image=front_card)

    flipping = window.after(3000, flip_card)


def flip_card():
    global card
    en_word = card['English']
    
    canvas.itemconfig(word_label, text=en_word, fill="white")
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(img, image=back_card)


# images
canvas = Canvas(window, width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
x_image = PhotoImage(file="./images/wrong.png")
checkmark = PhotoImage(file="./images/right.png")
front_card = PhotoImage(file="./images/card_front.png")
back_card = PhotoImage(file="./images/card_back.png")

img = canvas.create_image(400, 263, image=front_card)

canvas.grid(row=0, column=0, columnspan=2)

# Labels
title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word_label = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))

# Buttons
wrong_button = Button(image=x_image, bg=BACKGROUND_COLOR, highlightthickness=0, borderwidth=0, command=lambda: gen_word_fr(check=False))
wrong_button.grid(row=1, column=0)

check_button = Button(image=checkmark, bg=BACKGROUND_COLOR, highlightthickness=0, borderwidth=0, command=lambda: gen_word_fr(check=True))
check_button.grid(row=1, column=1)

gen_word_fr(False)

window.mainloop()