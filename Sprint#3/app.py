from types import MethodDescriptorType
from flask import Flask, app, json, render_template, request, flash, redirect, url_for, jsonify, session
from flask_session import Session
from funcion import registro, login,crearActivity
import os


""" Controladores """
from validarForms import iniciarSesion
from usersControllers import cantUsers, sql_insert_users, getUsers, getUser,getActivity,setnote,sql_insert_activity,getEstudiante,getAsignatura



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
@app.route('/LoginAdministrativo', methods=['GET','POST']) 
@app.route('/LoginAdministrativo/<sesion>', methods=['GET','POST']) 
def loginA(sesion = None):
    form = login()

    if sesion != None:
        if sesion == "signout":
            session.clear()

            return redirect("/LoginAdministrativo")
    else:
        if form.validate_on_submit():
	        return render_template('base.html')

    return render_template('loginAdm.html', form = form)

# Login de Estudiantes
@app.route('/LoginEstudiantes',methods=['GET','POST']) 
@app.route('/LoginEstudiantes/<sesion>', methods=['GET','POST'])
def loginE(sesion=None): 
    form = login()
    if sesion != None:
        if sesion == "signout":
            session.clear()
            return redirect("/LoginEstudiantes")
    else:
        if form.validate_on_submit():
	        return render_template('base.html')
    return render_template('loginEst.html',form=form)

# Login de Docentes
@app.route('/LoginDocentes',methods=['GET','POST']) 
@app.route('/LoginDocentes/<sesion>', methods=['GET','POST']) 
def loginD(sesion=None): 
    form = login()
   
    if sesion != None:
        if sesion == "signout":
            session.clear()

            return redirect("/LoginDocentes")
    else:
        if form.validate_on_submit():
	        return render_template('baseDocentes.html')

    return render_template('loginDoc.html',form=form)





# Validación de Inicio de Sesión
@app.route("/valogin", methods=["POST"])
def validarLogin():
    user = request.form["user"]
    pss = request.form["pass"]

    sesion = iniciarSesion(user, pss)
    if (sesion['Inicio'] == "Correcto"):
        session['nombre'] = sesion['datos'][2]
    else:
        sesion = {"Inicio": "error"}
    
    return(jsonify(sesion))





""" DashBoards """
# Dashboard - Administrador
@app.route('/DashBoard-Administrativo', methods=['GET','POST']) 
def dashboard(): 
    if 'nombre' in session:
        return render_template('base.html')
    else: 
        return redirect(url_for("loginA"))


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
        
    return render_template('registrar.html', form = form)

@app.route('/DashBoard-Administrativo/buscador',methods=['GET','POST'])
def buscador():
    if request.method == "POST":
        cc = request.form["cc"]

        user = getUser(cc)
        return(jsonify(user))
    return render_template("buscar-Pro-Est.html")


#Mockups docente

@app.route('/DashBoard-Docentes', methods=['GET', 'POST'])
def dashDocente():
    if 'nombre' in session:
        return render_template('baseDocente.html')
    else: 
        return redirect(url_for("loginD"))

@app.route('/DashBoard-Docentes/overview', methods=['GET', 'POST'])
def doc_overview():
    return render_template('overdocente.html')


@app.route('/DashBoard-Docentes/buscarActividad', methods=['GET', 'POST'])
def buscarActiRetro():

    return render_template("buscarActividad.html")


@app.route('/DashBoard-Docentes/buscarActividad/retroalimentarActividad/<cod>/<idAct>', methods=['GET','POST'])
def retroalimentar(cod,idAct):
    if request.method == "GET":
        act = getActivity(cod,idAct)
        return render_template("retroActividad.html", data = act)

    return render_template("buscarActividad.html")

#actualizar nota
@app.route('/DashBoard-Docentes/buscarActividad/retroalimentarActividad/<cod>', methods=['POST'])
def actualizarNota(cod):
    nota=request.form['nota-obtenida']
    #aun falta
   

#Crear actividad
@app.route('/DashBoard-Docentes/crearActividad', methods=['GET','POST'])
def crearAct():
    form=crearActivity(request.form)
    if request.method=='POST':
        id=request.form['id_Act']
        des=request.form['descripcion']
        sql_insert_activity(id,des)
        flash("Actividad creada")
        return redirect('crearActividad')

    return render_template('crearActividad.html',form=form)

@app.route('/DashBoard-Docentes/buscar', methods=['GET', 'POST'])
def buscar():
    return render_template("paginaBuscar.html")
  

@app.route('/DashBoard-Docentes/buscar/estudiante', methods=['GET', 'POST'])
def buscar1():
    if request.method == "POST":
        cc = request.form["cc"]
        user = getEstudiante(cc)
        return(jsonify(user))
  


@app.route('/DashBoard-Docentes/buscar/asignatura', methods=['GET', 'POST'])
def buscar2():
    if request.method == "POST":
        cc = request.form["cc"]
        user = getAsignatura(cc)
        return(jsonify(user))
  


#mockups buscar Actividad y retroalimentar, y buscar y resultados de busqueda



if __name__=="__main__":
    app.run(host = '127.0.0.1', port = 443, ssl_context = ('micertificado.pem', 'llaveprivada.pem'))
 