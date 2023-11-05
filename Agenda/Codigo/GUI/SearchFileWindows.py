from tkinter import  Tk as tk,Label,Entry,Button
import os as direct



#Codigo de Ventana
class buscador():
    def __init__(self) :
        self.ventana=tk()
        self.etiquetaNameProcess = Label(self.ventana, text="Instroduce ruta del .csv que quieras importar ")
        self.etiquetaNameProcess.pack()
        self.InputDir = Entry(self.ventana)
        self.InputDir.pack()
        self.Button=Button(self.ventana,text="Importar",command=self.encontrarDatos)
        self.Button.pack()
           
        self.ventana.mainloop()
        
        pass
    def encontrarDatos(self):
        existe= self.ComprobarPath(self.InputDir.get())
        print(existe)
        if (existe):
            ListFich=direct.listdir(self.InputDir.get())
            print(ListFich)
        else:
            print("RUTA NO EXISTE")
        
       
       
    def ComprobarPath(self,Newruta):
    #comprobamos Ruta pasada
        try:
            direct.listdir(Newruta)
            return True
        except:
            print("la Ruta no es valida")
        return False
        
        pass