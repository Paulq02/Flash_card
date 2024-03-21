from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"



screen = Tk()
screen.minsize(width=800, height=526)
screen.title("Flashy")
screen.config(background=BACKGROUND_COLOR, padx=50, pady=50)


def words_to_learn():
    global updated_list
    word_list.remove(current_card)  # type: ignore
    updated_list = pandas.DataFrame(word_list)
    if len(updated_list) == 0: 
        my_canvas.itemconfig(word_card, text="Great Job!")
        my_canvas.itemconfig(title_card, text="Complete!")
    updated_list.to_csv("/home/paulq02/Desktop/flash-card-project-start/data/words_to_learn.csv", index=False)
    next_word()
    

    
    


def english():
    
    my_canvas.itemconfig(card_color, image=c_back_img)
    my_canvas.itemconfig(title_card, text="English")
    my_canvas.itemconfig(word_card, text=current_card["English"])
    



def next_word():
    global current_card, flip_timer
    
    screen.after_cancel(flip_timer)
    current_card = random.choice(word_list)
    
    my_canvas.itemconfig(card_color, image=c_front_img)
    my_canvas.itemconfig(title_card, text="Spanish")
    my_canvas.itemconfig(word_card, text=current_card["Spanish"])
    flip_timer = screen.after(3000, english)
    
    
    



c_front_img = PhotoImage(file="/home/paulq02/Desktop/flash-card-project-start/images/card_front.png")
c_back_img = PhotoImage(file="/home/paulq02/Desktop/flash-card-project-start/images/card_back.png")

wrong_picture = PhotoImage(file="/home/paulq02/Desktop/flash-card-project-start/images/wrong.png")
right_picture = PhotoImage(file="/home/paulq02/Desktop/flash-card-project-start/images/right.png")

try:
    word_list = pandas.read_csv("/home/paulq02/Desktop/flash-card-project-start/data/words_to_learn.csv")

except FileNotFoundError:

    word_file = pandas.read_csv("/home/paulq02/Desktop/flash-card-project-start/data/Spanish_words.csv")
    word_list = word_file.to_dict(orient="records")
else:
    word_list = word_list.to_dict(orient="records")
    




my_canvas = Canvas(height=526, width=800)
my_canvas.config(bg=BACKGROUND_COLOR, highlightbackground=BACKGROUND_COLOR)


card_color = my_canvas.create_image(400, 263, image=c_front_img )
title_card = my_canvas.create_text(400,150,text="",font=("Ariel",40, "italic"))
word_card = my_canvas.create_text(400, 263,text="",font=("Ariel",60, "bold"))

my_canvas.grid(column=0, row=0, columnspan=2)


w_button = Button(image=wrong_picture, command=next_word)
w_button.config(borderwidth=0, highlightbackground=BACKGROUND_COLOR)
w_button.grid(row=1, column=0)


r_button = Button(image=right_picture, command=words_to_learn)
r_button.config(borderwidth=0, highlightbackground=BACKGROUND_COLOR)
r_button.grid(row=1, column=1)

flip_timer = screen.after(3000, english)
next_word()







screen.mainloop()



