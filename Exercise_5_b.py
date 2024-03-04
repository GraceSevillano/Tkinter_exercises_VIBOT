#from tkinter import *
import tkinter as tk
root = tk.Tk()
root.geometry('1000x1000')
myCanvas = tk.Canvas(root,width=2000, height=2000, bg='white')
#myCanvas.pack()
#myCanvas.pack()
#colornew = StringVar()



def create_circle(x, y, r, canvasName,color): 
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    canvasName.create_oval(x0, y0, x1, y1,width=10,outline=color)
    #canvasName.pack()
    #print(color)
    #colornew.set("blue")

bBLUE = tk.Button(root, text='Draw Blue', command=lambda: create_circle(300, 200, 100, myCanvas,color="blue"))
bRED = tk.Button(root, text='Draw black', command=lambda:create_circle(500, 200, 100, myCanvas,color="black"))
bYELLOW =tk.Button(root, text='Draw red', command=lambda:create_circle(700, 200, 100, myCanvas,color="red"))
bBLACK = tk.Button(root, text='Draw yellow', command=lambda:create_circle(400, 300, 100, myCanvas,color="yellow"))
bGREEN = tk.Button(root, text='Draw Green', command=lambda:create_circle(600, 300, 100, myCanvas,color="green"))


#b1.pack()
bBLUE.pack()
bBLACK.pack()
bRED.pack()
bYELLOW.pack()
bGREEN.pack()

b1 = tk.Button(root, text='Quit', command=root.quit)

b1.pack()
myCanvas.pack()

#bRED.pack()
#bYELLOW.pack()
#bBLACK.pack()
#bGREEN.pack()



#create_circle(50, 25, 10, myCanvas)
root.mainloop()