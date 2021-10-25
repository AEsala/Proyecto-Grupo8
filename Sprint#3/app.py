from types import MethodDescriptorType
from flask import Flask, app, json, render_template, request, flash, redirect, url_for, jsonify, session
from flask_session import Session
from funcion import registro,login
import os


""" Controladores """
from validarForms import iniciarSesion
from usersControllers import cantUsers, sql_insert_users, getUsers, getUser,getActivity



app = Flask(__name__) 
app.secret_key = os.urandom(24)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Rutas Mockup 1 inicio-2login-3 dashboard
@app.route('/',methods=['GET','POST']) 
def index(): 
    return render_template("inicio.html")


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





# Validación de Inicio de Sesión
@app.route("/valogin", methods=["POST"])
def validarLogin():
    user = request.form["user"]
    pss = request.form["pass"]

    sesion = iniciarSesion(user, pss)
    if (sesion['Inicio'] == "Correcto"):
        session['nombre'] = sesion['datos'][2]
    
    return(jsonify(sesion))





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
    cantEst = cantUsers()
    users = getUsers()
    data = {
        "cant": cantEst,
        "users": users
    }
    return render_template('estudiantes.html', students = data)



@app.route('/DashBoard-Administrativo/docentes',methods=['GET','POST'])
def docentes():
    return render_template('docentes.html')


@app.route('/DashBoard-Administrativo/cursos',methods=['GET','POST'])
def cursos():
    return render_template('cursos.html')


@app.route('/DashBoard-Administrativo/registrar',methods=['GET','POST'])
def nuevo_usuario():
    form = registro(request.form)
    if request.method == 'POST':
        primerNombre = request.form['primerNombre']
        segundoNombre = request.form['segundoNombre']
        primerApellido = request.form['primerApellido']
        segundoApellido = request.form['segundoApellido']
        codUsuario = request.form['codUsuario']
        direccion = request.form['direccion']
        email = request.form['email']
        clave = request.form['clave']
        typeUser = request.form["entradalista1"]
        
        sql_insert_users(primerNombre, segundoNombre, primerApellido, segundoApellido, codUsuario, email, clave, typeUser)
        flash("Registro Exitoso")
        return redirect('registrar')
        
    return render_template('registrar.html',form=form)

@app.route('/DashBoard-Administrativo/buscador',methods=['GET','POST'])
def buscador():
    if request.method == "POST":
        cc = request.form["cc"]
        user = getUser(cc)
        return(jsonify(user))

    return render_template("buscar-Pro-Est.html")


#Mockups docente



@app.route('/DashBoard-Administrativo/docentes/buscarActividad', methods=['GET', 'POST'])
def buscarActiRetro():
    if request.method == "POST":
        codUsuario = request.form["codUsuario"]
        details = getActivity(codUsuario)
        
        return(jsonify(details))
    return render_template("buscarActividad.html")

@app.route('/DashBoard-Administrativo/docentes/buscarActividad/retroalimentarActividad/<cod>', methods=['GET','POST'])
def retroalimentar(cod):
    return render_template("retroActividad.html")        

@app.route('/DashBoard-Administrativo/docentes/buscar', methods=['GET', 'POST'])
def buscar():
    return render_template("paginaBuscar.html")

@app.route('/DashBoard-Administrativo/docentes/buscar/resultados', methods=['GET','POST'])
def mostrarRes():
    return render_template("resultadosBusqueda.html")

#mockups buscar Actividad y retroalimentar, y buscar y resultados de busqueda



if __name__=="__main__":
    app.run(host = '127.0.0.1', port = 443, ssl_context = ('micertificado.pem', 'llaveprivada.pem'))
 