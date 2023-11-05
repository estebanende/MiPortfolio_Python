from tkinter import *
from tkinter import Tk as tk
from conexion.conectar import *
from RunProccess import *
class modifyWindows():
    def __init__(self,ventanaMain,mail) :
        self.Ventana=tk()
        self.ventanaMain=ventanaMain
        BloquarCampos(self.ventanaMain)
        self.Mailrecogido=mail
        datosUsuario=self.Sacardatos()
        self.etiquetaNameProcess = Label(self.Ventana, text="Nombre del Contacto")
        self.etiquetaNameProcess.pack()
        self.Nombre=Entry(self.Ventana)
        self.Nombre.insert(0,datosUsuario[0][0])
        self.Nombre.pack()
        self.etiquetaDescription = Label(self.Ventana, text="Descripcion del contacto")
        self.etiquetaDescription.pack()
        self.InputDescription = Entry(self.Ventana)
        self.InputDescription.insert(0,datosUsuario[0][1])
        self.InputDescription.pack()
        self.etiquetaNameProcess = Label(self.Ventana, text="Email")
        self.etiquetaNameProcess.pack()
        self.NombreMail=Entry(self.Ventana)
        self.NombreMail.insert(0,datosUsuario[0][2])
        self.NombreMail.pack()
        self.NombreMail.config(state=DISABLED)
        self.BotonSave=Button(self.Ventana,text="Guardar",command=self.guardarRegistro)
        self.BotonSave.pack()
        self.Ventana.protocol("WM_DELETE_WINDOW", self.eventcerrar)
        self.Ventana.mainloop()
        
    def Sacardatos(self):
        print("entro aqui")        
        conex,curosr=conectar()
        sql = "SELECT * FROM T_USER WHERE Email = ?"
        self.Mailrecogido
  
        if curosr.execute(sql,( self.Mailrecogido,)):
            resultado=curosr.fetchall() 
        else:
            print("Fallo")
        
        conex.close()
        return resultado
    def guardarRegistro(self):
        conex,curosr=conectar()
        datosUpdate=[self.Nombre.get(),self.InputDescription.get(),self.NombreMail.get()]
        print(datosUpdate)
        sql = "UPDATE T_USER  SET Name=? , Description=? WHERE Email = ?"
        if (curosr.execute(sql,datosUpdate)):
            print("se actualizo !!")
            conex.commit()
        else:
            print("error")   
        conex.close()
        ActivarCampos(self.ventanaMain)
        self.Ventana.destroy()
    def eventcerrar(self):
        self.Ventana.destroy()
        ActivarCampos(self.ventanaMain)
        print("se ha cerrado la ventana")
        

