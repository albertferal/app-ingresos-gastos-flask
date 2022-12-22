from flask import Flask

app = Flask(__name__)

from app_registro.routes import * #así hago referencia a todas las rutas definidas dentro de route.py

#inicializamos servidor Flask:
    #em mac: export FLASK_APP=main.py
    #en windows: set FLASK_APP=main.py

# flask --app main --debug run