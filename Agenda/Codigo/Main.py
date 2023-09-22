#En este proyecto vamos a simular un sistemas de automatizacion de procesos  en el cual podremos lanzar procesos de 
# forma automatica por ejemplo que me envie todo los días un correo dandome los buenos días o que ejecute una limpieza de ordenador
# Tendremos un filtro  con un grid para que podamos buscar cual queramos 
# podremos añadir y mmodificar contactos existentes 
# tendremos un boton de borrrar contacto
# tendremos una opcion de exportar los contactos a .csv para llevarnoslo a cualquier lado 
#Tendremos una opcion de importar csv que nos añadira los contactos  
from conexion.conectar import  *
from GUI.MainWindows import *   

if __name__ == '__main__':
    CrearTablas()
    MyWindows= mainWindows()
    
    pass    

