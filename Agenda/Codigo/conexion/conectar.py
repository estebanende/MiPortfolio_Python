'''
Clase para hacer conexion con nuestro sqlLite y de esta forma poder tener Guardado los datos una vez se 
cierre la aplicacion
para ello vamos a importar nuestro sqlLite
'''
import sqlite3

def conectar():
    
    conexion=sqlite3.connect("./Agenda/BDLite/miBD.db")
    cursor=conexion.cursor()
    return conexion,cursor

def CrearTablas():
    conex,cursor=conectar()
    table='''CREATE TABLE IF NOT EXISTS T_User( 
           Name varchar(200),
            Description varchar(200),
            Email varchar(200) primary key not null )
    '''
    if cursor.execute(table):
        print("TABLA CREADA!!! ")
    else:
        print("La tabla no ha podido ser creda")
    cerrarConexion(conex)
    
def cerrarConexion(conexion):
    conexion.close()



