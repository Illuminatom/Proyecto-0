def verificarinicio(a: str):
    A = a.upper()
    b = "ROBOT_R"
    if A == b:
        print("Yes")
    else: 
        print("No "+A)

#verificarigualdad("roBOT_R")

def verificarVARS(vars: str):
    if vars.__contains__(";"):
        varsNoEspacios = vars.split(" ")
        for i in varsNoEspacios:
            varsNoEspacios += i
    
        print(type(varsNoEspacios))


def verificarPROCS(proc: str):
    if (proc.__contains__("[") and proc.__contains__("]")):
        print("Yes")
    else:
        print("Nop")

def leerarchivotxt(nombreArchivo: str):
    nArchivo = nombreArchivo+".txt"
    fichero = open(nArchivo)
    inicio = fichero.readline()[:-1]

    #verificarinicio(inicio)

    vars1 = fichero.readline()[:-1]

    verificarVARS(vars1)

leerarchivotxt("archivo")



