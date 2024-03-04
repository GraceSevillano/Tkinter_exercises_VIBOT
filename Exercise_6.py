import tkinter as tk
from tkinter import ttk, IntVar
import random
from decimal import Decimal


def move_stars():

    c.delete('all')

    random_shift_1 = random.randint(100, 200)
    random_shift_2 = random.randint(100, 200)

    updated_center_1= random_shift_1
    updated_center_2= random_shift_2

    star_1_center.set(updated_center_1)
    star_2_center.set(updated_center_2)

    distance = "Distance between stars: "+str(abs(updated_center_2-updated_center_1))

    mass = "Mass of start 1: 100 \n Mass of start 2: 500"

    gravitational_force =  ((6.67*10**(-11) ) * 100 * 500 )/(updated_center_2-updated_center_1)**2 

    sttt = '%.2E' % Decimal(gravitational_force)

    print(sttt, type(sttt))

    grav = "Gravitational force:"+sttt
    
    star_1 = c.create_oval(star_1_center.get()-10, star_1_center.get()-10, star_1_center.get()+10, star_1_center.get()+10, width=5,outline="red", fill="red")#create_arc(x-r, y-r, x+r, y+r, **kwargs)

    star_2 = c.create_oval(star_2_center.get()-10,star_2_center.get()-10, star_2_center.get()+10, star_2_center.get()+10, width=5,outline="gray", fill="gray")#create_arc(x-r, y-r, x+r, y+r, **kwargs)



    c.create_text(150, 10, text=distance, fill="black", font=('Helvetica 15 bold'))
    c.create_text(150,40, text=mass, fill="black", font=('Helvetica 15 bold'))

    c.create_text(150,70, text=grav, fill="black", font=('Helvetica 15 bold'))

root = tk.Tk()
root.geometry()
c = tk.Canvas(root,bg="sky blue")  

star_1_center = IntVar()
star_2_center = IntVar()

star_1_center.set(50)
star_2_center.set(200)





rings_colors = ["blue", "yellow", "black", "green", "red"]


center_x = 50
center_y = 200
radius =  100




star_1 = c.create_oval(star_1_center.get()-10, star_1_center.get()-10, star_1_center.get()+10, star_1_center.get()+10, width=5,outline="red", fill="red")#create_arc(x-r, y-r, x+r, y+r, **kwargs)

star_2 = c.create_oval(star_2_center.get()-10,star_2_center.get()-10, star_2_center.get()+10, star_2_center.get()+10, width=5,outline="gray", fill="gray")#create_arc(x-r, y-r, x+r, y+r, **kwargs)


b1 = tk.Button(root, 
          text='Quit', 
          command=root.quit)

b1 = tk.Button(root, 
          text='Move Stars', 
          command=move_stars)
c.pack()
b1.pack()

root.mainloop()