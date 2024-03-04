import tkinter as tk
class App():
    def __init__(self, L_CUADRADO): 
        self.L_CUADRADO=L_CUADRADO

        self.ventana=tk.Tk()
        self.ventana.title("Ajedrez")
        self.ventana.geometry(f"{str(L_CUADRADO*8)}x{str(L_CUADRADO*8)}") 
        self.interfaz=tk.Canvas(self.ventana)
        self.interfaz.pack(fill="both",expand=1)
        self.ventana.resizable(0,0)

    def __call__(self):
        self.ventana.mainloop()

    def cuadrado(self):
        for i in range(8):
            for j in range(8):
                if (i+j)%2==0:
                    self.interfaz.create_rectangle(i*self.L_CUADRADO,j*self.L_CUADRADO,(i+1)*self.L_CUADRADO, (j+1)*self.L_CUADRADO, fill="white")

                else:
                    self.interfaz.create_rectangle(i*self.L_CUADRADO,j*self.L_CUADRADO, (i+1)*self.L_CUADRADO, (j+1)*self.L_CUADRADO, fill="black")



Ajedrez=App(70)
Ajedrez.cuadrado()
Ajedrez()
