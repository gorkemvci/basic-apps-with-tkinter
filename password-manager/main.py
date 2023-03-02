import tkinter
from PIL import ImageTk, Image 
import random
import string
import json
FONT = ("Comic Sans MS",10, "bold") 
window = tkinter.Tk()
window.title("PASSWORD ADMINISTOR")

def create_button_func():
    text_password.delete(0,"end")
    password=""
    for i in range(5):
        lwrcase=random.choice(string.ascii_lowercase)
        upcase=random.choice(string.ascii_uppercase)
        punc=random.choice(string.punctuation)
        digits=random.choice(string.digits)
        password=password + lwrcase + upcase + punc + digits
    text_password.insert(-1,password)  
def add_button_func():
    website = text_website.get()
    email = text_email.get()
    password = text_password.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    try:  
        with open("Passport Manager/data.json", "r") as data_file:
            data = json.load(data_file)
    except:
         with open("Passport Manager/data.json", "w") as data_file:
            json.dump(new_data,data_file,indent=4)
    else:
        with open("Passport Manager/data.json", "w") as data_file:
            data.update(new_data)
            json.dump(data,data_file,indent=4)
    finally:
         text_password.delete(0,"end")
         text_website.delete(0,"end")
         
def search_button_func():
    website = text_website.get()
    try:  
        with open("Passport Manager/data.json", "r") as data_file:
            data = json.load(data_file)
            if website in data:
                pass
            else:
               pass
    except:
        pass
    else:
        pass
window.config(padx=100,pady=175)
window.minsize(600,600)
label_title= tkinter.Label(text="My Password Administor",font=FONT)
logo = "Passport Manager/locker.png"
image_logo = Image.open(logo)
image_logo_show = ImageTk.PhotoImage(image_logo)
label_logo = tkinter.Label(image=image_logo_show)
label_website = tkinter.Label(text="Website",font=FONT)
label_email= tkinter.Label(text="Email",font=FONT)
label_password= tkinter.Label(text="Password",font=FONT)
text_website = tkinter.Entry(font=FONT, width=35)
text_email = tkinter.Entry(font=FONT, width=35)
text_password = tkinter.Entry(font=FONT, width=35)
button_search = tkinter.Button(text="Search", width=12, font=FONT, command=search_button_func)
button_create = tkinter.Button(text="Create Password",font=FONT, command=create_button_func)
button_add = tkinter.Button(text="Add New Website or Change",font=FONT,command=add_button_func)
label_title.grid(column=1,row=0)
label_logo.grid(column = 1,row = 1)
label_website.grid(column = 0,row = 2)
label_email.grid(column = 0,row = 3)
label_password.grid(column = 0,row = 4)

text_website.grid(column = 1,row = 2 )
text_email.grid(column = 1,row =3)
text_password.grid(column = 1,row =4)

button_search.grid(column=3,row=2)
button_create.grid(column=3,row=4)
button_add.grid(column=0,row=5)



window.mainloop()