from flask_wtf import FlaskForm,Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, length,InputRequired


class registro(FlaskForm):
    nombre =StringField('Nombres :',validators=[DataRequired(message='No dejar vacío, completar')])
    apellido =StringField('Apellidos :',validators=[DataRequired(message='No dejar vacío, completar')])
    cedula=StringField('Cedula :',validators=[DataRequired(message='No dejar vacio,completar')])
    direccion=StringField('Direccion :',validators=[DataRequired(message='No dejar vacío, completar')])
    email=EmailField('Correo :',validators=[DataRequired(message='No dejar vacío, completar')])
    celular=StringField('Celular :',validators=[DataRequired(message='No dejar vacío, completar')])
    enviar=SubmitField('Registrar')

class login(FlaskForm):
    usuario=StringField('Usuario :',validators=[DataRequired(message='No dejar vacío, completar')])
    password=PasswordField('Contraseña :',validators=[DataRequired(message='No dejar vacío, completar')])
    inicio_sesion=SubmitField('Iniciar Sesión')
