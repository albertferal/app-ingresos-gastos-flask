from flask import Flask

app = Flask(__name__)

from app_registro.routes import * #así hago referencia a todas las rutas definidas dentro de route.py

#inicializamos servidor Flask:
    #em mac: export FLASK_APP=main.py
    #en windows: set FLASK_APP=main.py

#otra alternativa sería crear el archivo oculto .env y dentro agregar los siguientes comandos:
#FLASK_APP=main.py
#FLASK_DEBUG=True
# flask --app main --debug run