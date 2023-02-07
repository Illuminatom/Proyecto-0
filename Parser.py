
import sys
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
"""
def leerarchivotxt(nombreArchivo: str):
    nArchivo = nombreArchivo+".txt"
    fichero = open(nArchivo)
    inicio = fichero.readline()[:-1]

    #verificarinicio(inicio)

    vars1 = fichero.readline()[:-1]

    verificarVARS(vars1)

leerarchivotxt("archivo")
"""
Do = True

def printMenu():
    while Do:
            
        print("\n")
        print("*******************************************")
        print("Bienvenido")
        
        print("\n")
        print("SELECCIONE UNA DE LAS SIGUIENTES OPCIONES")
        print("\n")
        print("1-INGRESAR TEXTO A ANALIZAR") #TO-DO Cargar archivo 
        print("2- REQ 1 - OPCION ADICIONAL")
        print("0- Salir")
        option = input("Opcion a elegir: ")
        if option == "1":
            txt = input("Ingrese aquí el texto, de momento \n no se carga un archivo")
            partido = txt.split(",")
        elif option == "2":
            print("Has elegido la segunda opción")
            #entrada = input("entrada de prueba")
        else:
            Do == False
    print("*******************************************")
print(printMenu())