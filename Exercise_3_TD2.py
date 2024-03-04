from tkinter import *

ventanita = Tk()

menubar = Menu(ventanita)
ventanita.config(menu=menubar)


def abrir_ventana_secundaria():
    
    ventana_secundaria = Toplevel()
    ventana_secundaria.title("Operation")
    ventana_secundaria.config(width=300, height=200)
    
    boton_transfer = Button(ventana_secundaria,text="Transfer",command=ventana_secundaria.destroy)
    boton_transfer.place(x=75, y=75)
    boton_transac = Button(ventana_secundaria,text="Transaction",command=ventana_secundaria.destroy)
    boton_transac.place(x=200, y=75)

    boton_cerrar = Button(ventana_secundaria,text="Close",command=ventana_secundaria.destroy)
    boton_cerrar.place(x=90, y=150)


filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New",command=abrir_ventana_secundaria)
filemenu.add_command(label="Open")
filemenu.add_command(label="Save")
#filemenu.add_command(label="Close")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=ventanita.quit)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cortar")
editmenu.add_command(label="Copiar")
editmenu.add_command(label="Pegar")

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Ayuda")
helpmenu.add_separator()
helpmenu.add_command(label="Acerca de...")

menubar.add_cascade(label="Archivo", menu=filemenu)
menubar.add_cascade(label="Editar", menu=editmenu)
menubar.add_cascade(label="Ayuda", menu=helpmenu)

# Finalmente bucle de la aplicación
ventanita.mainloop()
