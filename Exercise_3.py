from tkinter import *
import random
ventanita= Tk()
myCanvas = Canvas(ventanita)
myCanvas.grid(column=0, row=0, sticky=(N, W, E, S))

colornew = StringVar()
colors = ['purple', 'cyan', 'green', 'red', 'blue', 'orange', 'black'] 


def create_circle(): 

    r = random.randint(10,40)
    x = random.randint(50,250)
    y = random.randint(50,250)

    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    
    myCanvas.create_oval(x0, y0, x1, y1,fill= colornew.get())

    print(x,y,r)

def change_color():
    colornew.set(random.choice(colors))

def clear():
    colornew.set("blue")
    myCanvas.delete('all')

b1 = Button(ventanita, text='Draw circle', width=10,bg='green',command=lambda: create_circle())
b1.grid(row=1,column=3)

b1 = Button(ventanita, text='Change color', width=10,bg='green',command=lambda: change_color())
b1.grid(row=2,column=3)

b4 = Button(ventanita,text='Clear',bg='gray', command=lambda:clear())
b4.grid(row=3,column=3)

ventanita.mainloop()