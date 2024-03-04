from tkinter import *

ventana = Tk()  
ventana.title('Registro')



Label(ventana, text="Prenom").grid(row=0)
Label(ventana, text="Nom").grid(row=1)
Label(ventana, text="Date de naissance").grid(row=2)

def campos():
    palabra = "\t"+entrada2.get()+ " "+ entrada1.get()+" was born on "+entrada3.get()+"/"+entrada4.get()+"/"+entrada5.get()
    
    l1 = Label(ventana, text=palabra,background="Yellow").grid(row=4,column=2)

entrada1 = Entry(ventana)
entrada2 = Entry(ventana)


validate_entry = lambda text: text.isdecimal()
entrada3 = Entry(ventana,validate="key",validatecommand=(ventana.register(validate_entry), "%S"))
entrada4 = Entry(ventana,validate="key",validatecommand=(ventana.register(validate_entry), "%S"))
entrada5 = Entry(ventana,validate="key",validatecommand=(ventana.register(validate_entry), "%S"))

entrada1.grid(row=0, column=1)
entrada2.grid(row=1, column=1)
entrada3.grid(row=2, column=1)
entrada4.grid(row=2, column=2)
entrada5.grid(row=2, column=3)

Button(ventana, text='Quit', command=ventana.quit,bg='Red').grid(row=3, column=1, sticky=W, pady=4)
Button(ventana, text='Show', command=campos, bg='green').grid(row=3, column=3, sticky=W,pady=4)

ventana.mainloop()