import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title('Background')
ventana.geometry('500x250')

ttk.Label(ventana, text = "Ejercicio",
        background = 'Purple', foreground ="white",
        font = ("Times New Roman", 15)).grid(row = 0, column = 1)

ttk.Label(ventana, text = "Select the color :",
        font = ("Times New Roman", 10)).grid(column = 0,
        row = 5, padx = 10, pady = 25)

n = tk.StringVar()
colorelegido = ttk.Combobox(ventana, width = 27, textvariable = n)

colores = ["red","green","yellow","white","blue","green","sky blue","black","gray","sky blue","black","gray"]
colorelegido['values'] = colores

colorelegido.grid(column = 1, row = 5)
colorelegido.current()

#cuadro=tk.Entry(colorelegido)


def update(elegido):

    print("---",elegido)

    colores.append(elegido)
    colorelegido['values'] = colores
    colorelegido.bind('<<ComboboxSelected>>', color_cambiado)
    ventana.configure(bg=elegido)
    ventana.update()

def color_cambiado(event):

    color = colorelegido.get()
    ventana.configure(bg=color)
    ventana.update()

def remove_color():
    picked_color = colorelegido.get()
    colorelegido.current()
    colores.remove(picked_color)

    colorelegido['values'] = colores

    print(colores)
    colorelegido.delete(0,"end")
    colorelegido.bind('<<ComboboxSelected>>', color_cambiado)

def añadir():
    num = colorelegido.get()
    #print("---",elegido)
    colores.append(num)
    
    values=list(colorelegido["values"])
    colorelegido["values"]=values+[num]
    print(colores)


colorelegido.bind('<<ComboboxSelected>>', color_cambiado)
colorelegido.bind('<Return>', lambda event, entry=colorelegido, text="s":
                                    update(entry.get()))

#tk.Label(ventana, text="Add Color").grid(row=8)

b1 = tk.Button(ventana, text='Quit', command=ventana.quit)
b2 = tk.Button(ventana, text='Remove selected color',command=remove_color)
b3 = tk.Button(ventana, text='Add Color',command=añadir)

b1.grid(column=3, row=6)
b2.grid(column=3, row=7)
b3.grid(column=3, row=8)
ventana.mainloop()
