import datetime 

from Tkinter import *

root = Tk()

v = IntVar()
v.set(1)  # initializing the choice, i.e. Python

stations = [
    ("Poorani Jeans",1),
    ("Filmy Gaane",2),
    ("Ghazals",3),
    ("Metal",4),
    ("Cheesy",5)
]

def connectStation():
    station = v.get()

Label(root, 
      text="""Choose your favourite 
Radio Station:""",
      justify = LEFT,
      padx = 20).pack()

for txt, val in stations:
    Radiobutton(root, 
                text=txt,
                padx = 20, 
                variable=v, 
                command=connectStation,
                value=val).pack(anchor=W)

mainloop()