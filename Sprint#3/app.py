from flask import Flask ,app,render_template
from funcion import registro,login
import os

app = Flask(__name__) 
app.secret_key=os.urandom(24)

# Rutas Mockup 1 inicio-2login-3 dashboard
@app.route('/',methods=['GET','POST']) 
def index(): 
    return render_template('inicio.html')

@app.route('/LoginAdministrativo',methods=['GET','POST']) 
def loginA(): 
    form=login()  
    if form.validate_on_submit():
		    return render_template('base.html')
    return render_template('loginAdm.html', form=form)

@app.route('/LoginEstudiantes',methods=['GET','POST']) 
def loginE(): 
    form=login()
    return render_template('loginEst.html',form=form)

@app.route('/LoginDocentes',methods=['GET','POST']) 
def loginD(): 
    form=login()
    return render_template('loginDoc.html',form=form)

@app.route('/DashBoard-Administrativo',methods=['GET','POST']) 
def dashboard(): 
    return render_template('base.html')

@app.route('/DashBoard-Administrativo/overview',methods=['GET','POST'])
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

@app.route('/DashBoard-Administrativo/registrar',methods=['GET','POST'])
def registrar():
    form=registro()
    return render_template('registrar.html',form=form)

#Mockups docente

@app.route('/DashBoard-Administrativo/docentes/buscarActividad',methods=['GET', 'POST'])
def index():
    return render_template("buscarActividad.html")

@app.route('/DashBoard-Administrativo/docentes/buscarActividad/retroalimentarActividad',methods=['GET','POST'])
def resultado():
    return render_template("retroActividad.html")        

@app.route('/DashBoard-Administrativo/docentes/buscar')
def buscar():
    return render_template("paginaBuscar.html")

@app.route('/DashBoard-Administrativo/docentes/buscar/resultados')
def mostrarRes():
    return render_template("resultadosBusqueda.html")

if __name__=="__main__":
    print("Entro al main")
    app.run(debug=True,port=5000)    


