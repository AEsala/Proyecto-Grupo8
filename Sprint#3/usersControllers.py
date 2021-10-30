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



# Método para Obtener estudiantes
def getUsers():
    connect = get_db()
    cursor = connect.cursor()
    sql = " SELECT idUsuario, primerNombre, segundoNombre, primerApellido, segundoApellido, codUsuario, email FROM Usuarios WHERE idTipoUsuario = 1"
    cursor.execute(sql)
    users = cursor.fetchall()
    return users
#metodo para obtener profesores
def getUsers1():
    connect = get_db()
    cursor = connect.cursor()
    sql = " SELECT idUsuario, primerNombre, segundoNombre, primerApellido, segundoApellido, codUsuario, email FROM Usuarios WHERE idTipoUsuario = 2"
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

def cantUsers1():
    connect = get_db()
    cursor = connect.cursor()
    sql = " SELECT COUNT(*) FROM Usuarios WHERE idTipoUsuario = 2; "
    cursor.execute(sql)
    users = cursor.fetchone()
    return users

def getCurso():
    connect = get_db()
    cursor = connect.cursor()
    sql = " SELECT idCurso,descripcion FROM Cursos"
    cursor.execute(sql)
    cursos = cursor.fetchall()
    return cursos

def cantCurso():
    connect = get_db()
    cursor = connect.cursor()
    sql = " SELECT COUNT(*) FROM Cursos; "
    cursor.execute(sql)
    cursos = cursor.fetchone()
    return cursos

def getUser(cc):
    connect = get_db()
    cursor = connect.cursor()
    sql = "SELECT * FROM Usuarios WHERE codUsuario = {}".format(cc)
    cursor.execute(sql)
    user = cursor.fetchone()

    return user


#Metodo para buscar actividad

def getActivity(codUsuario, idAct):
    connect = get_db()
    cursor = connect.cursor()
    sql = " SELECT * FROM Detalle_Notas "
    sql += " JOIN Comentarios ON Comentarios.idComentario = Detalle_Notas.idComentario "
    sql += " WHERE codUsuario = ? AND idActividad = ?; "
    cursor.execute(sql, [codUsuario, idAct])
    details = cursor.fetchone()
    return details




#metodo para actualizar nota de actividad
def setNote(cod, nota):
    connect = get_db()
    cursor = connect.cursor()
    
    sql =  " UPDATE Detalle_Notas SET notaActividad = ? WHERE codUsuario = ? "
    cursor.execute(sql, [nota, cod])
    connect.commit()
    connect.close()


def setComent(idComent, coment):
    connect = get_db()
    cursor = connect.cursor()
    
    sql =  " UPDATE Comentarios SET descripcion = ? WHERE idComentario = ?; "
    cursor.execute(sql, [coment, idComent])
    connect.commit()
    connect.close()



#crear actividad 
def sql_insert_activity( id, description):
    
    newAct = [id,description]

    sql = " INSERT INTO Actividades (idActividad,descripcion) VALUES (?, ?); "

    conn = get_db()       
    cursor = conn.cursor()        
    cursor.execute(sql,newAct)
    print("actividad registrada")

    conn.commit()
    conn.close()


def getEstudiante(cc):
    connect = get_db()
    cursor = connect.cursor()
    sql = "SELECT * FROM Usuarios WHERE codUsuario = {} AND idTipoUsuario=1".format(cc)
    cursor.execute(sql)
    user = cursor.fetchone()
    return user

def getAsignatura(id):
    connect = get_db()
    cursor = connect.cursor()
    sql = "SELECT * FROM Asignaturas WHERE idAsignatura={}".format(id) 
    cursor.execute(sql)
    actividad = cursor.fetchone()
    return actividad

#crear curso 
def sql_insert_curso(id,descripcion):
    newCurso = [id,descripcion]
    sql = " INSERT INTO Cursos (idCurso,descripcion) VALUES (?, ?); "
    conn = get_db()       
    cursor = conn.cursor()        
    cursor.execute(sql, newCurso)
    print("Curso Registrado en la base de datos")
    conn.commit()
    conn.close()