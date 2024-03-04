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

def line(): 

    #r = random.randint(10,20)
    x0 = random.randint(0,400)
    y0 = random.randint(0,400)
    x1 = random.randint(0,400)
    y1 = random.randint(0,400)
    #x0 = x - r
    #y0 = y - r
    #x1 = x + r
    #y1 = y + r
    
    myCanvas.create_line(x0, y0,x1,y1, fill=colornew.get(), width=5)

    #print(x,y,r)

def triangle(): 

    #r = random.randint(10,20)
    #x = random.randint(50,250)
    #y = random.randint(50,250)

    a1 = random.randint(0,400)
    b1 = random.randint(0,400)
    a2 = random.randint(0,400)
    b2 = random.randint(0,400)
    a3 = random.randint(0,400)
    b3 = random.randint(0,400)
    
    myCanvas.create_polygon(a1, b1, a2, b2, a3, b3, fill=colornew.get(), width=5)

    print(a1, b1, a2, b2, a3, b3)

def change_color():
    colornew.set(random.choice(colors))

def clear():
    colornew.set("blue")
    myCanvas.delete('all')

b1 = Button(ventanita, text='Draw circle', width=10,bg='green',command=lambda: create_circle())
b1.grid(row=1,column=3)

b2 = Button(ventanita, text='Draw line', width=10,bg='yellow',command=lambda: line())
b2.grid(row=2,column=3)

b3 = Button(ventanita, text='Draw triangle', width=10,bg='purple',command=lambda: triangle())
b3.grid(row=3,column=3)

b4 = Button(ventanita, text='Change color', width=10,bg='green',command=lambda: change_color())
b4.grid(row=4,column=3)

b5 = Button(ventanita,text='Clear',bg='gray', command=lambda:clear())
b5.grid(row=5,column=3)


b6 = Button(ventanita,text='Quit',bg='red', command=ventanita.quit)
b6.grid(row=6,column=3)

ventanita.mainloop()