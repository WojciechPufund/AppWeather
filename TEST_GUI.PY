from tkinter import *
from tkinter.ttk import *


root = Tk()
root.title("Weather Aplication")
root.geometry('400x400')
lbl = Label(root, text = "Enter city name")
lbl.grid()

txt = Entry(root, width=10)
txt.grid(column=1,row=0)

Label(root, text = 'GeeksforGeeks', font =('Verdana', 15))
Label.pack(side = TOP, pady = 10)
# photo = PhotoImage(file = r"C:\Users\pufun\logo.png")

def clicked(): 
    res = ("You wrote ")
    lbl.configure(text = res)

btn = Button(root, text = "Click me" ,fg = "red", command=clicked).grid(column=2, row=0)






root.mainloop()