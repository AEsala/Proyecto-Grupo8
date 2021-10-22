from types import MethodDescriptorType
from flask import Flask ,app,render_template,request,flash,redirect,url_for
from funcion import registro,login
import os

from sqlite3 import Error
from db import get_db


app = Flask(__name__) 
app.secret_key = os.urandom(24)

# Rutas Mockup 1 inicio-2login-3 dashboard
@app.route('/',methods=['GET','POST']) 
def index(): 
    return render_template('inicio.html')


""" Logins """
# Login del Administrador
@app.route('/LoginAdministrativo',methods=['GET','POST']) 
def loginA(): 
    form = login() 

    if form.validate_on_submit():
	    return render_template('base.html')

    return render_template('loginAdm.html', form = form)

# Login de Estudiantes
@app.route('/LoginEstudiantes',methods=['GET','POST']) 
def loginE(): 
    form = login()
    return render_template('loginEst.html',form=form)

# Login de Docentes
@app.route('/LoginDocentes',methods=['GET','POST']) 
def loginD(): 
    form = login()
    return render_template('loginDoc.html',form=form)


""" DashBoards """
# Dashboard - Administrador
@app.route('/DashBoard-Administrativo',methods=['GET','POST']) 
def dashboard(): 
    return render_template('base.html')

@app.route('/DashBoard-Administrativo/overview',methods=['GET'])
def overview():
    return render_template('overview.html')


@app.route('/DashBoard-Administrativo/estudiantes',methods=['GET','POST'])
def estudiantes():
    return render_template('estudiantes.html')

@app.route('/DashBoard-Administrativo/docentes',methods=['GET','POST'])
def docentes():
    return render_template('docentes.html')


@app.route('/DashBoard-Administrativo/cursos',methods=['GET','POST'])
def cursos():
    return render_template('cursos.html')

# @app.route('/DashBoard-Administrativo/registrar')
# def registrar():
#     form=registro()
#     return render_template('registrar.html',form=form)


@app.route('/DashBoard-Administrativo/registrar',methods=['GET','POST'])
def nuevo_usuario():
    form=registro(request.form)
    if request.method == 'POST':
        primerNombre = request.form['primerNombre']
        segundoNombre = request.form['segundoNombre']
        primerApellido = request.form['primerApellido']
        segundoApellido = request.form['segundoApellido']
        codUsuario = request.form['codUsuario']
        direccion = request.form['direccion']
        email = request.form['email']
        clave = request.form['clave']
        
      
        sql_insert_users(primerNombre,segundoNombre,primerApellido,segundoApellido,codUsuario,direccion,email,clave)
        flash("Registro Exitoso")
        return redirect('registrar')
        

    return render_template('registrar.html',form=form)

@app.route('/DashBoard-Administrativo/buscador',methods=['GET','POST'])
def buscador():
    return render_template('buscar-Pro-Est.html')

#Mockups docente



@app.route('/DashBoard-Administrativo/docentes/buscarActividad',methods=['GET', 'POST'])
def buscarActiRetro():
    return render_template("buscarActividad.html")

@app.route('/DashBoard-Administrativo/docentes/buscarActividad/retroalimentarActividad',methods=['GET','POST'])
def retroalimentar():
    return render_template("retroActividad.html")        

@app.route('/DashBoard-Administrativo/docentes/buscar', methods=['GET', 'POST'])
def buscar():
    return render_template("paginaBuscar.html")

@app.route('/DashBoard-Administrativo/docentes/buscar/resultados', methods=['GET','POST'])
def mostrarRes():
    return render_template("resultadosBusqueda.html")

#mockups buscar Actividad y retroalimentar, y buscar y resultados de busqueda


#Funciones para conectarse con la base de datos 
def sql_insert_users(primerNombre,segundoNombre,primerApellido,segundoApellido,codUsuario,direccion,email,clave):
    try:
        sql = "INSERT INTO Producto (primerNombre,segundoNombre,primerApellido,segundoApellido,codUsuario,direccion,email,clave) VALUES ('{}','{}','{}','{}')".format(primerNombre,segundoNombre,primerApellido,segundoApellido,codUsuario,direccion,email,clave)
        print(sql)
        conn = get_db()       
        cursorObj = conn.cursor()        
        cursorObj.execute(sql)
        print("Usuario Registrado en la base de datos")
        conn.commit() 
        conn.close()
    except Error:
        print(Error)

if __name__=="__main__":
    app.run(debug = True, port = 5000)    