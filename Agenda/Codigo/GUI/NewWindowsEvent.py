from tkinter import Tk as tk
from tkinter import *
from tkinter import  Toplevel, Label, Entry, Text, Button
from conexion.conectar import  *


class WindowsNewEvent():
    def __init__(self,ventanaPrincipal):
        
        self.ventanMain=ventanaPrincipal
        print(self.ventanMain)
        self.ventana = tk()
        #self.ventana=Toplevel(ventanaPrincipal)
        self.ventana.title("Nuevo Contacto")
        self.etiquetaNameProcess = Label(self.ventana, text="Nombre del Contacto")
        self.etiquetaNameProcess.pack()
        self.InputNombre = Entry(self.ventana)
        self.InputNombre.pack()
        self.etiquetaDescription = Label(self.ventana, text="Descripcion del contacto")
        self.etiquetaDescription.pack()
        self.InputDescription = Text(self.ventana, height=3, width=30)
        self.InputDescription.pack()
        self.etiquetaMail = Label(self.ventana, text="Mail")
        self.etiquetaMail.pack()
        self.InputMail = Entry(self.ventana)
        self.InputMail.pack()
        
        self.ButtonSave=Button(self.ventana,text="Guardar",command=self.Guardar )
        self.ButtonSave.pack()
        self.ventana.mainloop()
        

    def Guardar(self):
        self.ventana.update()
        inputnombre = self.InputNombre.get()
        InputDescription = self.InputDescription.get("1.0", "end-1c")
        inputMail=self.InputMail.get()
        parametros=[inputnombre,InputDescription,inputMail]
        chequeo= self.chequearParametros(parametros)
        if chequeo==True:
            conex,cursor=conectar()
            sql='''INSERT INTO T_User(Name,Description,Email)  VALUES (?,?,?)'''
            if cursor.execute(sql,parametros):
                print("ejecutado de forma correcta ")
                conex.commit()
              
                self.ventana.destroy()
            
            conex.commit()
            conex.close()
                
                    
                  
        
        for widget in self.ventanMain.winfo_children():
               
                if not   isinstance(widget, Frame):
                    widget.config(state=ACTIVE)
       
        
        
        
    def chequearParametros(self,parametros):
        retorno=True
        #1º chequo se comprueba si de los campos son blancos
        for comprobacion in  parametros:
            print(comprobacion)
            if comprobacion.strip()=="":
                print("el campo es blanco")
                retorno=False
        #2º Chequo se debe comprobar que no exista ese Mail  sepodia haber creado el maiol como clave 1º pero no ha sido el caso
        conex,cursor=conectar()
        sql1='''SELECT COUNT(*)  FROM T_User WHERE Email= ? '''
        mail=parametros[2]
        cursor.execute(sql1,(mail,))
        resultado=cursor.fetchone()
        if resultado[0] >0:
            retorno=False
            print("el mail existe")
             
        conex.close()
        
        
        return retorno