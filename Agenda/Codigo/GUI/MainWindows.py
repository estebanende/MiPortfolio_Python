'''
Clase para pantalla principal con la cual creamos la ventana y todo sus eventos en un futuro la crearemos  con tkinter
pero por ahora solo vamos a realiza el back
'''
from tkinter import Tk as tk
from tkinter import *
from GUI.NewWindowsEvent import *
from RunProccess import *
class mainWindows:
    def __init__(self) :
        super().__init__()
       
        self.ventana=tk()
        self.inicio=0
       
        self.ventana.title("Aplicación")
        self.gridTable=Frame(self.ventana,height=500,width=900 )
        self.gridTable.pack()
        #self.GridtableBody=Frame(self.gridTable,height=500,width=1000)
        self.LabelMail=Label(self.gridTable,text="Buscador")
        self.LabelMail.grid(row=0,column=1)
        self.buscadorMail=Entry(self.gridTable,textvariable="Introcue un Mail para buscarlo")
        self.buscadorMail.grid(row=1,column=1)
        self.buscadorMail.bind("<KeyRelease>",self.MosrtrarregisotrsGRID)
        #creamos la cabezera de la tabla que se rellenara mas adelante en la funcion MosrtrarregisotrsGRID
        self.headerName=Entry(self.gridTable,fg="blue",border=1)
        self.headerName.insert(0,"Name")
        self.headerName.grid(row=2,column=1)
        self.headerDescriprion=Entry(self.gridTable,fg="blue",border=1)
        self.headerDescriprion.insert(0,"Description")
        self.headerDescriprion.grid(row=2,column=2)
        self.headerEmail=Entry(self.gridTable,fg="blue",border=1)
        self.headerEmail.insert(0,"Email")
        self.headerEmail.grid(row=2,column=3)
        #self.GridtableBody.pack()
       #para comprobar que es la 1º vez
        if self.inicio==0:
            print("entramos en if de refresh")
            self.inicio+=1
            self.MosrtrarregisotrsGRID("")
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
        self.ventana.update()
        print(self.ventana.winfo_children())
        '''
        esta forma de desactivar los componetes no es valia ya que los fgrame no se pueden desactivar 
         for widget in self.ventana.winfo_children():
            print(widget)
            widget.config(state=DISABLED)
       '''
        self.boton_insertar.config(state=DISABLED)
        self.boton_modificar.config(state=DISABLED)
        self.boton_eliminar.config(state=DISABLED)
       # self.buscadorMail.config(state=DISABLED)
        
        WindowsNewEvent(self.ventana)
    
        pass
    
    def ModifyEvent(self):
        print("entro en modificar")
        pass
    
    def deleteEvent(self):
        print("Borramos evento")
        pass
    def MosrtrarregisotrsGRID(self,event):
        
        email= self.buscadorMail.get()
        resultado= MostrarConsultaGrid(email)
        self.LimpiarGrid()
        columna=1
        fila=3
        for row in resultado:
            fila=fila+1
            columna=1
            print(row)
            for columnas in row:
                
                columLabel=Entry(self.gridTable,fg="red",border=1)
                columLabel.insert(0,str(columnas))
                columLabel.grid(row=fila,column=columna)
                columna=columna+1
        pass
    def LimpiarGrid(self):
    # Obtén todos los widgets dentro del gridTable
        for widget in self.gridTable.winfo_children():
            print(widget)
            if widget not in [self.buscadorMail, self.LabelMail, self.headerName,self.headerDescriprion,self.headerEmail] and not isinstance(widget, Frame):
                widget.destroy()
    
    