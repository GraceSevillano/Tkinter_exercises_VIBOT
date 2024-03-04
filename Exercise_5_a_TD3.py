import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from calendar import month_name
import time 

root = tk.Tk()
root.geometry('1000x1000')
c = tk.Canvas(root,bg='white')  

rings_colors = ["blue", "yellow", "black", "green", "red"]


center_x = 50
center_y = 200
radius =  100

for i,color in enumerate(rings_colors):

    print(i)

    i+=1

    if i % 2 == 0:
        center_x += 50
        center_y += 20

    else:
        center_x += 50
        center_y -= 20

    xr = center_x+int(radius/2)
    yr= center_y+int(radius/2)
    x_r = center_x-int(radius/2)
    y_r= center_y-int(radius/2)
    c.create_oval(xr, yr, x_r, y_r, width=5, outline=color)#create_arc(x-r, y-r, x+r, y+r, **kwargs)

c.pack()

b1 = tk.Button(root, 
          text='Quit', 
          command=root.quit)

b1.pack()


root.mainloop()
