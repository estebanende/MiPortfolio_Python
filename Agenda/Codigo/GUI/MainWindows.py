'''
Clase para pantalla principal con la cual creamos la ventana y todo sus eventos en un futuro la crearemos  con tkinter
pero por ahora solo vamos a realiza el back
'''
from tkinter import Tk as tk
from tkinter import *


class mainWindows:
    def __init__(self) :
        #super().__init__()
        self.ventana=tk()
        self.ventana.title("Aplicación")
        
        self.etiqueta = Label(self.ventana, text="Seleccione una opción:")
        self.etiqueta.pack()
        
        self.boton_insertar = Button(self.ventana, text="Insertar", command=self.registryEvent)
        self.boton_insertar.pack()
        
        self.boton_modificar = Button(self.ventana, text="Modificar", command=self.ModifyEvent)
        self.boton_modificar.pack()
        
        self.boton_eliminar = Button(self.ventana, text="Eliminar", command=self.deleteEvent)
        self.boton_eliminar.pack()
        self.ventana.mainloop()
        
        pass
        
    def registryEvent(self):
        print("entro en registºrar evento")
        pass
    
    def ModifyEvent(self):
        print("entro en modificar")
        pass
    
    def deleteEvent(self):
        print("Borramos evento")
        pass
    
    