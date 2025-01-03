from flask import Flask,render_template,request,url_for,redirect
from DB.crud import AccesoDB

resultado = None #variable null en python

App = Flask(__name__)

registroUsuario = AccesoDB

@App.route("/")
def index():
    name = 'logo'
    return render_template("index.html",name = name)

@App.route("/reg/<name>")
def registroCargar(name):
    return render_template("index.html",name = name)

@App.route("/form", methods=['POST'])
def registro():
    nombre= request.form['nombre']
    edad = int(request.form['edad'])
    telefono = int(request.form['telefono'])
    email = request.form['email']
    resultado = registroUsuario.insert(nombre,edad,telefono,email)
    #redirect: redirecciona a una ruta 
    #url_for: devuelve el nombre de la ruta 
    return render_template('index.html', resultado = resultado)

@App.route("/lista")
def lista():
    name = 'list'
    lista =registroUsuario.select()
    return  render_template("index.html",lista = lista,name = name)

@App.route("/delete/<id>", methods = ['GET'])
def eliminar(id):
    ide = int(id)
    registroUsuario.delete(ide)
    return redirect(url_for("lista"))

@App.route('/form/actualizar/<name>/<id>')
def formActualizar(name,id):
    ide = int(id)
    persona =registroUsuario.consulta(ide)
    return render_template('index.html',persona = persona,name = name)

@App.route('/actualizar/<id>', methods = ['POST'])
def actualizar(id):
    ide = int(id)
    nombre= request.form['nombre']
    edad = int(request.form['edad'])
    telefono = int(request.form['telefono'])
    email = request.form['email']
    registroUsuario.update(ide,nombre,edad,telefono,email)
    return redirect(url_for('lista'))

if __name__ == '__main__':
    App.run(host='localhost',port=4000,debug=True)