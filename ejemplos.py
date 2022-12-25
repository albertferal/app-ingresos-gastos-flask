#lectura de acrhivos

with open ("data/movimientos.txt", "r") as resultado:

    leer = resultado.read()

    print(leer)