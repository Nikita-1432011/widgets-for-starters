from tkinter import *
from datetime import date
window = Tk()
window.title("getting started with activity of widgets")
window.geometry("500x500")
lbl= Label (text = "hey there , wellcome", fg="white",bg="black", height=1,width=20) 
name_lbl = Label (text= "Full Name", bg= "blue")
name_entry = Entry ()
text_box = Text (height=10, width=200)
def display():
    name = name_entry.get()
    global Message
    message = "welcome to the application for the first time \nToday's date is:"
    greet = "Hello" +name+"\n"
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())
btn = Button (text="begin", command= display, height=2, width=10, bg="blue", fg ="black")
lbl.pack()
name_lbl.pack()
name_entry.pack()
text_box.pack()
btn.pack()
window.mainloop()


