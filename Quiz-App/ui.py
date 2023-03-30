import tkinter
from questions import Question
import html
class uiQuiz():
    
    def __init__(self,BGCOLOR,FONT):
        self.BGCOLOR = BGCOLOR
        self.FONT = FONT
        self.question = str
        self.answer = str
        self.counter = 0
        self.score = 0
        self.question_number =  10
        self.difficulty = "Easy"
        self.category = "Shuffle"
        self.window = tkinter.Tk()
        self.window.config(padx=30,pady=30)
        self.window.config(background=self.BGCOLOR[0])
        self.window.title("QUIZzzz APP")
        self.area_thema = tkinter.Canvas(height=300,width=300)
        self.text = self.area_thema.create_text(150,150, width=280, text="Quiz-App\nGörkem AVCI", font= self.FONT) 
        self.text_one = self.area_thema.create_text(120,220, width=280, text=f" Questions-Number: {self.question_number} " 
                                               f"\n Difficulty: {self.difficulty}\n Category: {self.category}", font= self.FONT)     
        self.button_start_img= tkinter.PhotoImage(file="Tkinter\Quiz-App\start.png")
        self.button_settings_img = tkinter.PhotoImage(file="Tkinter\Quiz-App/settings.png")
        self.button_start= tkinter.Button(image=self.button_start_img, command=self.start_func)
        self.button_settings= tkinter.Button(image=self.button_settings_img, command=self.settings_func)
        self.label = tkinter.Label(bg=self.BGCOLOR[0])
        self.label.grid(row= 0, column=1)
        self.button_start.grid(row= 2, column=0)
        self.button_settings.grid(row= 2, column=2)
        self.area_thema.grid(row= 1, column=0, columnspan=3, pady=50)


        self.window.mainloop()

    def settings_func(self):

            pass

    def start_func(self):
        self.label.config(text=f"Score: {self.score}/{self.counter}", bg=self.BGCOLOR[0], font=self.FONT)
        self.area_thema.delete(self.text_one)
        self.button_start.destroy()
        self.button_settings.destroy()
        self.button_right_img= tkinter.PhotoImage(file="Quiz-App/right.png")
        self.button_wrong_img = tkinter.PhotoImage(file="Quiz-App/wrong.png")
        self.button_right= tkinter.Button(image=self.button_right_img, command=self.right_func)
        self.button_wrong= tkinter.Button(image=self.button_wrong_img, command=self.wrong_func)
        self.button_right.grid(row= 2, column=0)
        self.button_wrong.grid(row= 2, column=2)   
        self.question_func()

    def question_func(self):
        if self.counter == 10:
            self.button_right.destroy()
            self.button_wrong.destroy()
            self.label.config(text=f"GAME IS END \nScore: {self.score}/{self.counter}", bg=self.BGCOLOR[0], font=self.FONT)
        else:
            self.label.config(text=f"Score: {self.score}/{self.counter}", bg=self.BGCOLOR[0], font=self.FONT)
            self.area_thema.config(background="white")
            self.data = Question()
            self.question = html.unescape(self.data.data["results"][self.counter]["question"])
            self.answer = self.data.data["results"][self.counter]["correct_answer"]
            self.area_thema.itemconfig( self.text, text = self.question)
            self.counter = self.counter + 1

        print(self.answer)
        print(self.counter)

    def right_func(self):
        if self.answer == "True" :
            self.area_thema.config(background="green")
            self.score = self.score + 1
        else:
            self.area_thema.config(background="red")
        self.window.after(100,self.question_func)
    def wrong_func(self):
        if self.answer == "False" :
            self.area_thema.config(background="green")
            self.score = self.score + 1
        else:
            self.area_thema.config(background="red")
        self.window.after(100,self.question_func)
    