import tkinter  as tk 
from tkinter import ttk
from time import strftime

ventanita = tk.Tk()
ventanita.title('Reloj')
ventanita.geometry("200x200")  

def tiempo(): 
    time_string = strftime('%H:%M:%S %p')
    numero_str.set(time_string)  

numero_str=tk.StringVar()
N1 = tk.Label(ventanita, textvariable=numero_str,width=15) 
N1.grid(row=3,column=3) 

b1 = tk.Button(ventanita, text='Current Time', width=10,bg='green',command=lambda: tiempo())
b1.grid(row=1,column=3)

b2=tk.Button(ventanita, text='Quit', command=ventanita.quit).grid(row=4, 
                                    column=3)

ventanita.mainloop()
