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
            Id INTEGER primary key AUTOINCREMENT not null,
            Name varchar(200),
            Apellido varchar(200),
            Email varchar(200))
    '''
    if cursor.execute(table):
        print("TABLA CREADA!!! ")
    else:
        print("La tabla no ha podido ser creda")
    
    
    table='''CREATE TABLE IF NOT EXISTS T_PROCESS_DESCRIPTION_Mail( 
            Id INTEGER primary key not null,
            Id_Proccess INTEGER NOT NULL, 
            Name varchar(200),
            Description varchar(2000),
            Hour INTEGER,
            Active INTEGER(1))
    '''
    if cursor.execute(table):
        print("TABLA CREADA!!! ")
    else:
        print("La tabla no ha podido ser creda")
        
    table='''CREATE TABLE IF NOT EXISTS T_PROCESS( 
            Id_Proccess INTEGER primary key AUTOINCREMENT NOT NULL,
            processComand varchar(2000))
            '''
    if cursor.execute(table):
        print("TABLA CREADA!!! ")
    else:
        print("La tabla no ha podido ser creda")
    cerrarConexion(conex)
    
def cerrarConexion(conexion):
    conexion.close()



