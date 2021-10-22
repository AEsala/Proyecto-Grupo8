""" Importaciones """
from flask import jsonify
from db import get_db
from werkzeug.security import check_password_hash, generate_password_hash

def iniciarSesion(user, pss):
    if (len(user) >= 5) and (len(pss) >= 8):
        cursor = get_db().cursor()

        cursor.execute("SELECT * FROM Usuarios WHERE primerNombre = ?", [user])
        resultado = cursor.fetchone()

        validate = check_password_hash(resultado[7], pss)

        if validate == True:
            return(jsonify({
                "datos": resultado,
                "Inicio": "Correcto"
            }))
        else:
            return(jsonify({
                "Inicio": "Error"
            })) 
    else:
        return(jsonify("No se pudo iniciar sesión"))