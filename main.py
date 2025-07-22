from tkinter import *

screen = Tk()
screen.title("Mi - Kms Converter")
screen.minsize(width=400, height=400)
label = Label(text="Miles to Kilometers", font=("calibri", 24, "bold"))
label.place(x=20, y=50)
def button_click():
    #THIS GETS THE INPUT FROM THE BOX AND PUTS IT IN LABEL
    new_text = int(inpt.get())
    kilometers = new_text*1.60934
    label.config(text=str(new_text)+" Miles is \n"+str(round(kilometers, 2))+" Kilometers")
button = Button(text="Convert", command=button_click)
button.place(x=175, y=180)
#Entry component

inpt = Entry(width=10)
inpt.grid(column=1, row=4)
inpt.place(x=170, y=150)


screen.mainloop()



