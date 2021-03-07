#!/usr/bin/env python3
from tkinter import *
import tkinter as tk
from tkinter.font import Font
from tkinter import messagebox
import time
import random
import gaugelib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import pandas as pd


win = tk.Tk()
win.title("speedometer")
win.geometry("1700x900")
win.resizable(width=True, height=True)
win.configure(bg='black')

g_value=0
x=0
p3 = Scale(win,orient=VERTICAL,length=175,width=20,sliderlength=5,from_=0,to=100,tickinterval=100,troughcolor='light blue',label='Temperature',fg='white',bg='black')
p3.grid(row=2,column=1)
def read_every_second():
    global x
    g_value=random.randint(0,100)
    p1.set_value(int(g_value))
    g_value=random.randint(0,100)
    p2.set_value(int(g_value))
    g_value=random.randint(0,100)
    p3.set(int(g_value))
    x+=1
    if x>100:
        x=0
    win.after(100, read_every_second)

p1 = gaugelib.DrawGauge2(
    win,
    max_value=100,
    min_value=-0.0,
    size=200,
    bg_col='black',
    unit = "SPEED",bg_sel = 2)
p1.grid(row=1,column=0)

p2 = gaugelib.DrawGauge3(
    win,
    max_value=100,
    min_value=-0.0,
    size=200,
    bg_col='black',
    unit = "PRESSURE",bg_sel = 2)
p2.grid(row=1,column=2)


read_every_second()
x_values = []
y_values = []

fig,axes=plt.subplots(nrows=1,ncols=4,figsize=(14,3))
fig.patch.set_facecolor('pink')

fields=np.array(['temp','pressure','altitude','voltage'])

bar1 = FigureCanvasTkAgg(fig, win)
bar1.get_tk_widget().grid(row=3,columnspan=4)


data = pd.read_csv('/Users/vipul1/Downloads/data.csv')
time=data.index.to_numpy()
x_values = list(time)
for j in range(4):
        y_values = list(data[fields[j]].to_numpy())
        axes[j].clear()
        axes[j].plot(x_values, y_values,marker='o')
        axes[j].legend([fields[j]])
        axes[j].set_xlabel('Time')
        axes[j].set_ylabel(fields[j])
        axes[j].set_title(fields[j])
        axes[j].set_facecolor('black')
        
mainloop()
