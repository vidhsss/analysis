import math
import tkinter
from tkinter import *


def update_circle():
    w.create_oval(50, 50, 150, 150, fill="blue")
    return


def mod_calc(w1):
    slider_value = scale.get()
    remainder = number % slider_value
    if remainder == 0:
        update_circle()
        print('Factor: ', slider_value)
        return


number = int(input('Input number: '))
square_root = int(math.sqrt(number))

master = Tk()
w = Canvas(master)
w.pack()

w.create_oval(50, 50, 150, 150, fill="red")

w1 = Label(master, text="Input Number: " + str(number), font="Arial 16")
w1.pack()

w2 = Label(master, text="Square root: " + str(square_root), font="Arial 16")
w2.pack()

scale = Scale(master,
              from_=3, to=square_root,
              length=500,
              orient=HORIZONTAL,
              resolution=10,
              command=mod_calc)
scale.pack()

mainloop()