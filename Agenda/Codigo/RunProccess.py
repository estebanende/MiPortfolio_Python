from conexion.conectar import *
from tkinter import Tk as tk
from tkinter import *
from tkinter import  Toplevel, Label, Entry, Text, Button
from tkinter import ttk as ttkfrom


def MostrarConsultaGrid(Email):
    conex,curosr=conectar()
    sql = "SELECT * FROM T_USER WHERE Email LIKE ? || '%'"

  
    if curosr.execute(sql,(Email,)):
        resultado=curosr.fetchall()
       
        
    else:
        print("Fallo")
        
    conex.close()
    return resultado

def ActivarCampos(ventanaMain):
            for widget in ventanaMain.winfo_children():
               
                if not   isinstance(widget, Frame):
                    if type(widget)==Menu:
                        print("es un menú")
                    else:
                        widget.config(state=ACTIVE)
                   
                if    isinstance(widget, Frame):
                    for frame in widget.winfo_children():
                          frame.config(state=NORMAL)
        
       
            
            
def BloquarCampos(ventanaMain):
    
      for widget in ventanaMain.winfo_children():
                if not   isinstance(widget, Frame): 
                    if type(widget)==Menu:
                        print("es un menú")
                    else:
                        widget.config(state=DISABLED)
                    
                if    isinstance(widget, Frame):
                    for frame in widget.winfo_children():
                            frame.config(state=DISABLED)
        
        
def BorrarRegistro(mail):
    
    conex,curosr=conectar()
    sql = "DELETE  FROM T_USER  WHERE Email=? "

  
    if curosr.execute(sql,(mail,)):
       conex.commit()
       
       
        
    else:
        print("Fallo")
        
    conex.close()