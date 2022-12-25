from app_registro import app
from flask import render_template


@app.route("/")
def index():
    #prueba de diccionario a vista html
    datos = [
        {
            "Fecha": "18/12/2022",
            "Concepto": "Regalo de reyes",
            "Cantidad": "-275,50"
        }, 
        {
            "Fecha": "19/12/2022",
            "Concepto": "Cobro de trabajo",
            "Cantidad": "1200"
        }, 
        {
            "Fecha": "18/12/2022",
            "Concepto": "Ropa navidad",
            "Cantidad": "-355,50"
        }
    ]
    return render_template("index.html", pageTitle = "Listas", lista = datos)



@app.route("/new")
def create():
    return render_template("new.html", pageTitle = "Alta", typeAction="Alta", typeButton = "Guardar")

@app.route("/update")
def edit():
    return render_template("update.html", pageTitle = "Modificar", typeAction="Modificación", typeButton = "Editar")

@app.route("/delete")
def remove():
    return render_template("/delete.html", pageTitle = "Eliminar",  typeAction="Eliminar")