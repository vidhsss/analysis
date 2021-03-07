import tkinter as tk
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

data1 = {'Time': [1,2,3,5,7],
         'Pressure': [45000, 42000, 52000, 49000, 47000]
         }
df1 = DataFrame(data1, columns=['Time', 'Pressure'])

data2 = {'Time': [1,2,3,4,5,6,7,8,9,10],
         'Temp': [9.8, 12, 8, 7.2, 6.9, 7, 6.5, 6.2, 5.5, 6.3]
         }
df2 = DataFrame(data2, columns=['Time', 'Temp'])

data3 = {'Time': [5, 5.5, 6, 5.5, 5.25, 6.5, 7, 8, 7.5, 8.5],
         'Altitude': [1500, 1520, 1525, 1523, 1515, 1540, 1545, 1560, 1555, 1565]
         }
df3 = DataFrame(data3, columns=['Time', 'Altitude'])

root = tk.Tk()

figure1 = plt.Figure(figsize=(6, 5), dpi=100)
ax1 = figure1.add_subplot(111)
bar1 = FigureCanvasTkAgg(figure1, root)
bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
df1 = df1[['Time', 'Pressure']].groupby('Time').sum()
df1.plot(kind='line', legend=True, ax=ax1,marker='o')
ax1.set_title('Pressure Analysis')

figure2 = plt.Figure(figsize=(5, 4), dpi=100)
ax2 = figure2.add_subplot(111)
line2 = FigureCanvasTkAgg(figure2, root)
line2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
df2 = df2[['Time', 'Temp']].groupby('Temp').sum()
df2.plot(kind='line', legend=True, ax=ax2, color='r', marker='o', fontsize=10)
ax2.set_title('Temperature Anaysis')

figure3 = plt.Figure(figsize=(5, 4), dpi=100)
ax3 = figure3.add_subplot(111)
ax3.scatter(df3['Time'], df3["Altitude"], color='g')
scatter3 = FigureCanvasTkAgg(figure3, root)
scatter3.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
ax3.legend(['Altitude'])
ax3.set_xlabel('Time')
ax3.set_title('Altitude')

root.mainloop()