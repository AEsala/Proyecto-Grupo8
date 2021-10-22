from sqlite3 import Error

from werkzeug.security import generate_password_hash
from db import get_db
#Funciones para conectarse con la base de datos 
def sql_insert_users(primerNombre, segundoNombre, primerApellido, segundoApellido, codUsuario, email, clave, tipoUsuario):
    clave = generate_password_hash(clave)
    newUser = [codUsuario, primerNombre, segundoNombre, primerApellido, segundoApellido, email, clave, tipoUsuario]

    sql = " INSERT INTO Usuarios (idUsuario, codUsuario, primerNombre, segundoNombre, primerApellido, segundoApellido, email, clave, idTipoUsuario) VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?); "

    conn = get_db()       
    cursor = conn.cursor()        
    cursor.execute(sql, newUser)
    print("Usuario Registrado en la base de datos")

    conn.commit()
    conn.close()



# Método para Obtener todos los Usuarios
def getUsers():
    connect = get_db()
    cursor = connect.cursor()
    sql = " SELECT idUsuario, primerNombre, segundoNombre, primerApellido, segundoApellido, codUsuario, email FROM Usuarios "
    cursor.execute(sql)
    users = cursor.fetchall()

    return users

def cantUsers():
    connect = get_db()
    cursor = connect.cursor()
    sql = " SELECT COUNT(*) FROM Usuarios WHERE idTipoUsuario = 1; "
    cursor.execute(sql)
    users = cursor.fetchone()

    return users



def getUser(cc):
    connect = get_db()
    cursor = connect.cursor()

    sql = "SELECT * FROM Usuarios WHERE codUsuario = {}".format(cc)
    cursor.execute(sql)
    user = cursor.fetchone()

    return user


#Metodo para buscar actividad

def getActivity(cc):
    connect = get_db()
    cursor = connect.cursor()

    sql = "SELECT * FROM Usuarios WHERE codUsuario = {}".format(cc)
    cursor.execute(sql)
    user = cursor.fetchone()

    return user
