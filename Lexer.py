import os
import random

starters = ["ROBOT_R", "VARS", "PROCS"]
twoParametersCommands = ["assignto" ,"goto", "put", "pick", "movetothe", "moveindir", "jumptothe", "jumpindir"]
singleParameterCommands = ["move", "turn", "face"]
specialCharacters = [":", "|", ";", "]", "[", ","]
nop = "nop"
conditionals = ["if", "else", "then"]
loop = ["while", "do"]
twoParametersConditions = ["canput", "canpick", "canmoveindir", "canjumpindir", "canmovetothe", "canjumptothe", "not"]
singleParameterConditions = ["facing", "not"]

def esEspecial(string: str):
    """Retorna True si la cadena tiene un specialCharacter de lo contrario, retorna False"""
    i = 0
    while i <= len(string)-1:
        if string[i] in specialCharacters:
            return True
        elif ((i == len(string)-1)):
            return False

        i += 1

        
def definirNombresdeVariables(var: str):
    retorno = []
    nombre = ""

    if len(var) == 0:
        var = " "

    for char in var:
        if (esEspecial(char)):
            if nombre != "": retorno.append(nombre)
            
            retorno.append(char)            
            
            nombre = ""
        elif (char.isalnum()):
            nombre += char
        else:
            return "ERROR"

    if nombre != "":
        retorno.append(nombre)

    return retorno


def convertirATokens(listPalabras: list, listTokens: list):
    """Toma cada palabra de listPalabras y le asigna un token dependiendo de cual sea la palabra para posteriormente
    guardar cada token en listTokens en el orden de entrada"""
    for palabra in listPalabras:
        if (palabra.upper() in starters) or (palabra.lower() in conditionals) or (palabra.lower() in loop):
            listTokens.append(palabra.upper())
        elif (palabra.lower() in twoParametersCommands):
            listTokens.append("TwoParametersCommand")
        elif (palabra.lower() in singleParameterCommands):
            listTokens.append("SingleParameterCommand")
        elif (palabra.lower() in twoParametersConditions):
            listTokens.append("TwoParametersCondition")
        elif (palabra.lower() in singleParameterConditions):
            listTokens.append("SingleParameterCondition")
        elif (palabra in specialCharacters):
            listTokens.append(palabra) 
        else:
            nombres = definirNombresdeVariables(palabra)
            for nombre in nombres:
                if nombre not in specialCharacters:
                    listTokens.append("Name")
                else:
                    listTokens.append(nombre)
    

def lexer(archivo: str):
    strLineas = ""
    listPalabras = []
    listTokens = []
    nombreTxt = archivo+".txt"
    file = open(nombreTxt)

    fileList = file.readlines()

    i= 0                                                 #
    while i <= len(fileList)-1:                          #
        if i < len(fileList)-1:                          # Toma todas las lineas del archivo y las une en
            strLineas += " "+fileList[i][:-1]            # una sola cadena de caracteres (String)
        else:                                            #
            strLineas += " "+fileList[i]                 #
        i+=1                                             #
        

    listPalabras = strLineas.split()                     # Toma la cadena de caracteres anterior y la convierte
                                                         # en una lista cuyos elementos son todas las palabras
                                                         # omitiendo los espacios en blanco y las tabulaciones

    convertirATokens(listPalabras, listTokens)
    strTokens = " ".join(listTokens)

    print(strTokens)

    file.close()

    lexertxt = open("lexer{0}.txt".format(random.randint(0, 1000)), "x")

    lexertxt.write(strTokens)

    lexertxt.close()

lexer("archivo")