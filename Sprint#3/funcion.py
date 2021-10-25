from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, length,InputRequired

class registro(FlaskForm):
    primerNombre = StringField('Primer Nombre:', validators = [DataRequired(message='No dejar vacío, completar')])
    
    segundoNombre = StringField('Segundo Nombre:' )

    primerApellido = StringField('Primer Apellido:', validators = [DataRequired(message='No dejar vacío, completar')])
    
    segundoApellido = StringField('Segundo Apellido:' )
    
    codUsuario = StringField('Cedula:',  validators = [DataRequired(message='No dejar vacio,completar')])

    direccion = StringField('Direccion:',  validators = [DataRequired(message='No dejar vacío, completar')])

    email = EmailField('Correo:', validators = [DataRequired(message='No dejar vacío, completar')])

    clave = PasswordField('Clave:',  validators = [DataRequired(message='No dejar vacío, completar')])
  
    enviar = SubmitField('Registrar')


class login(FlaskForm):
    usuario = StringField('Usuario:', validators = [DataRequired(message='No dejar vacío, completar')])

    password = PasswordField('Contraseña:', validators = [DataRequired(message='No dejar vacío, completar')])
    
    inicio_sesion = SubmitField('Iniciar Sesión')
