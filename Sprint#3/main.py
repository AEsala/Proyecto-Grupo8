from flask import Flask ,app,render_template, request
from flask.json import jsonify
from funcion import registro, login
import os

app = Flask(__name__) 
app.secret_key=os.urandom(24)

# Rutas Mockup 1 inicio-2login-3 dashboard
@app.route('/',methods=['GET','POST']) 
def index(): 
    return render_template('index.html')

@app.route("/login/<user>")
def loginPage(user):
    form = login()  
    response = {
        "form": form,
        "type": user
    }
    return render_template("login.html", data = response)

if __name__=="__main__":
    print("Entro al main")
    app.run(debug=True,port=5000)    