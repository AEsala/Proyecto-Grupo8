from flask_wtf import FlaskForm,Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, length,InputRequired


class registro(FlaskForm):
    primer_nombre = StringField('Primer Nombre:', validators = [DataRequired(message='No dejar vacío, completar')])
    
    segundo_nombre = StringField('Segundo Nombre:' )

    primer_apellido = StringField('Primer Apellido:', validators = [DataRequired(message='No dejar vacío, completar')])
    
    segundo_apellido = StringField('Segundo Apellido:' )
    
    cedula = StringField('Cedula:',  validators = [DataRequired(message='No dejar vacio,completar')])

    direccion = StringField('Direccion:',  validators = [DataRequired(message='No dejar vacío, completar')])

    email = EmailField('Correo:', validators = [DataRequired(message='No dejar vacío, completar')])

    clave = StringField('Clave:',  validators = [DataRequired(message='No dejar vacío, completar')])

   
  
    enviar = SubmitField('Registrar')


class login(Form):
    usuario = StringField('Usuario:', validators = [DataRequired(message='No dejar vacío, completar')])

    password = PasswordField('Contraseña:', validators = [DataRequired(message='No dejar vacío, completar')])
    
    inicio_sesion = SubmitField('Iniciar Sesión')
