from conexion.conectar import *
def MostrarConsultaGrid(Email):
    conex,curosr=conectar()
    sql = "SELECT * FROM T_USER WHERE Email LIKE ? || '%'"

  
    if curosr.execute(sql,(Email,)):
        resultado=curosr.fetchall()
       
        
    else:
        print("Fallo")
        
    conex.close()
    return resultado