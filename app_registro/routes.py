from app_registro import app
from flask import render_template
import csv

@app.route("/")
def index():

    fichero = open("data/movimientos.txt","r") #llama al archivo
    csvReader = csv.reader(fichero, delimiter=",", quotechar='"') #accede a cada registro del archivo y lo formatea
    datos = [] #creamos array de datos para cargar los registros del archivo

    for item in csvReader:
        datos.append(item)

    return render_template("index.html", pageTitle = "Listas", lista = datos)



@app.route("/new", methods = ["GET", "POST"])
def create():
    return render_template("new.html", pageTitle = "Alta", typeAction="Alta", typeButton = "Guardar")

@app.route("/update")
def edit():
    return render_template("update.html", pageTitle = "Modificar", typeAction="Modificación", typeButton = "Editar")

@app.route("/delete")
def remove():
    return render_template("/delete.html", pageTitle = "Eliminar",  typeAction="Eliminar")