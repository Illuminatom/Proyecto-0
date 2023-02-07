import os
import time
import Lexer
import Parser

Do = True

def printMenu():
    while Do:
            
        print("\n")
        print("*******************************************")
        print("BIENVENIDO \n\n" +
        "El siguiente programa toma un archivo de nombre -archivo.txt- y le aplica LEXER, es decir \n" +
        "hace TOKENS de las entradas según corresponda, luego aplica PARSER y verifica si es \n"+
        "posible ejecutarlo para el robot del cual trata el proyecto. \n\n"+
        "NOTA: Verifique que el archivo se encuentre en la carpeta y tenga el nombre indica")
        
        print("\n")
        print("SELECCIONE UNA DE LAS SIGUIENTES OPCIONES")
        print("\n")

        print("1- CAMBIAR NOMBRE DOCUMENTO A ANALIZAR -Debe estar en la carpeta-")
        print("2- INICIAR PROCESO CON ARCHIVO GUARDADO -PREDETERMINADO archivo.txt-")
        print("3- OPCION ADICIONAL SIN USO")
        print("0- Salir")
        archivoLexer = "archivo"
        archivoSec = ""
        option = input("Opcion a elegir: ")
        if option == "1":
            print("Has elegido la primera opción\n\n")
            print("Recuerde que ya hay un archivo predeterminado seleccionado llamado: " + archivoLexer +  ".txt \n")
            conf = input("Si desea cambiar de igual manera el archivo ingrese -Y/y- : ")
            if conf == "Y" or conf == "y":
                archivoInput = input("Ingrese el nombre EXACTO del archivo a analizar sin la extensión .txt : \n")
                archivoCompleto = archivoInput + ".txt"
                print("El archivo ingresado es: " + archivoCompleto)
                file = os.path.exists(archivoCompleto)
                if file == True:
                    time.sleep(2)
                    print("El archivo se encuentra en carpeta y se ha cambiado exitosamente")
                    archivoLexer = archivoCompleto
                else:
                    time.sleep(1)
                    print("El archivo NO se encuentra en carpeta, se ha ingresado "+ archivoCompleto +" REVISE LO INGRESADO")
            else:
                print("No seleccionó algo válido se mantiene el actual archivo " + archivoLexer)
        elif option == "2":
            print("Has elegido la segunda opción\n\n")


            print("El nombre del archivo que se va a cargar es: " + archivoLexer + ".txt" "\n")

            time.sleep(2)

            print("La transformación a TOKENS del archivo seleccionado es la siguiente: \n")
            lexerExe = Lexer.lexer(archivoLexer) ### EN LA VARIABLE lexerExe se guarda el archivo TOKENIZADO 
            print(lexerExe)
        else:
            Do == False
    print("*******************************************")
print(printMenu())