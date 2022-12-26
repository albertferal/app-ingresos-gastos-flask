#lectura de acrhivos

with open ("data/movimientos.txt", "r") as resultado:

    leer = resultado.read()

    print(leer)
    print(type(leer))
    #result = open("data/movimientos.txt,"r"")
    #lectura = result.read()
    #print(lectura)