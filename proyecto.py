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

        print("1- INICIAR PROCESO CON ARCHIVO GUARDADO -PREDETERMINADO archivo.txt-")
        print("0- Salir")
        archivoLexer = "archivo"
        archivoSec = ""
        option = input("Opcion a elegir: ")

        if option == "1":
            print("Has elegido la segunda opción\n\n")


            print("El nombre del archivo que se va a cargar es: " + archivoLexer + ".txt" "\n")

            time.sleep(2)

            print("La transformación a TOKENS del archivo seleccionado es la siguiente: \n")
            lexerExe = Lexer.lexer(archivoLexer) ### EN LA VARIABLE lexerExe se guarda el archivo TOKENIZADO 
            print(lexerExe + "\n")

            Parser.parser(lexerExe)
        else:
            Do == False
    print("*******************************************")
print(printMenu())