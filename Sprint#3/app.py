from flask import Flask , render_template

app = Flask(__name__)

@app.route('/docente/buscarActividad')
def index():
    return render_template("buscarActividad.html")

@app.route('/docente/buscarActividad/retroalimentarActividad')
def resultado():
    return render_template("retroActividad.html")        

@app.route('/docente/buscar')
def buscar():
    return render_template("paginaBuscar.html")
