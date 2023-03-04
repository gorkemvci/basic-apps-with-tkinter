import tkinter
import pandas
import random
FONT = ("Comic Sans MS",20, "bold")
BGCOLOR = ["#AACB73","#3A98B9","#1F8A70",] 
data = pandas.read_csv("learn-english-words/data/vocabulary.csv")
words = data.to_dict(orient="records")
word =random.choice(words)
turn= True
def english_or_turkish_func():
    global turn
    if turn is  False:
        vocabulary_thema.itemconfig(card,image=turkish_img)
        vocabulary_thema.itemconfig(text,text=word.get("Turkish"))
        window.config(background=BGCOLOR[2])
        turn = True
    else:
        vocabulary_thema.itemconfig(card,image=english_img)
        vocabulary_thema.itemconfig(text,text=word.get("English"))
        window.config(background=BGCOLOR[1])
        turn = False
def true_or_wrong_func():
    global turn
    global word
    word =random.choice(words)
    turn = False
    vocabulary_thema.itemconfig(card,image=english_img)
    vocabulary_thema.itemconfig(text,text=word.get("English"))
    window.config(background=BGCOLOR[1])

def start_func(): 
    global turn
    english_or_turkish_func()
    button_start.config(image=button_turn_img, command=english_or_turkish_func)
    button_right.grid(row= 1, column=0)
    button_wrong.grid(row= 1, column=2)
    turn = False
def true_func():
   true_or_wrong_func()
def wrong_func():
   true_or_wrong_func()
window =  tkinter.Tk()
window.config(padx=50,pady=50)
window.config(background=BGCOLOR[0])
window.title("Learn Turkish - English")
vocabulary_thema = tkinter.Canvas(height=400,width=560)
english_img = tkinter.PhotoImage(file="Vocabulary/englishcard.png")
turkish_img = tkinter.PhotoImage(file="Vocabulary/turkishcard.png")
start_img = tkinter.PhotoImage(file="Vocabulary/startcard.png")
card =vocabulary_thema.create_image(280,200, image=start_img)
text = vocabulary_thema.create_text(280,210, text="hello", font=FONT)
vocabulary_thema.grid(row= 0, column=0, columnspan=3)

button_wrong_img= tkinter.PhotoImage(file="Vocabulary/wrong.png")
button_right_img= tkinter.PhotoImage(file="Vocabulary/right.png")
button_start_img= tkinter.PhotoImage(file="Vocabulary/start.png")
button_turn_img= tkinter.PhotoImage(file="Vocabulary/turn.png")
button_right= tkinter.Button(image= button_wrong_img, command=wrong_func)
button_wrong= tkinter.Button(image=button_right_img, command=true_func)
button_start= tkinter.Button(image=button_start_img, command=start_func)
button_start.grid(row= 1, column=1)
window.mainloop()