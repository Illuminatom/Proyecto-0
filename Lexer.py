import os
import random

starters = ["ROBOT_R", "VARS", "PROCS"]
directions = ["north", "south", "east", "west"]
orientations = ["left", "right", "front", "back"]
chipsOrballons = ["chips", "ballons"]
twoParametersCommands = ["assignto" ,"goto", "put", "pick", "movetothe", "moveindir", "jumptothe", "jumpindir"]
singleParameterCommands = ["move", "turn", "face"]
specialCharacters = [":", "|", ";", "]", "[", ","]
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
    numeros = ""

    if len(var) == 0:
        var = " "
        
    if (esEspecial(var) == False):
        if(var.isalnum()) and (var[0].isalpha()):
            retorno.append(var)
        else:
            return ["ERROR"]
    else:
        for char in var:
            if (esEspecial(char)):
                if nombre != "": retorno.append(nombre)

                retorno.append(char)            

                nombre = ""
            elif (char.isalpha()):
                nombre += char
                if numeros != "": retorno.append(numeros)
                numeros = ""

            elif (char.isnumeric()):
                numeros += char    
            else:
                return "ERROR"

    if nombre != "":
        retorno.append(nombre)
    
    if numeros != "":
        retorno.append(numeros)

    return retorno

def definirNombresPROCS(listaPalabras: list):
	listaPROCS = []
	i = 0 
	while i <= len(listaPalabras)-2:
		if listaPalabras[i][0].isalpha() and listaPalabras[i].isalnum():
			if "[" in listaPalabras[i+1]:
				listaPROCS.append(listaPalabras[i].lower())
		i += 1

	return listaPROCS

def convertirATokens(listPalabras: list, listTokens: list, listPROCS: list):
    """Toma cada palabra de listPalabras y le asigna un token dependiendo de cual sea la palabra para posteriormente
    guardar cada token en listTokens en el orden de entrada"""
    for palabra in listPalabras:
        if (palabra.upper() in starters) or (palabra.lower() in conditionals) or (palabra.lower() in loop):
            listTokens.append(palabra.upper())
        elif (palabra.lower() in twoParametersCommands):
            if("p" in palabra.lower()[0]):
                listTokens.append("TwoParametersCommand(n,X)")
            elif ("moveto" in palabra) or ("jumpto" in palabra):
                listTokens.append("TwoParametersCommand(n,O)")
            elif ("goto" in palabra.lower()):
                listTokens.append("TwoParametersCommand(n,n)")
            elif ("assignto" in palabra.lower()):
                listTokens.append("TwoParametersCommand(#,n)")
            else:
                listTokens.append("TwoParametersCommand(n,D)")

        elif (palabra.lower() in singleParameterCommands):
            if("move" in palabra.lower()):
                listTokens.append("SingleParameterCommand(n)")
            if("turn" in palabra.lower()):
                listTokens.append("SingleParameterCommand(O)")
            if("face" in palabra.lower()):
                listTokens.append("SingleParameterCommand(D)")

        elif (palabra.lower() in twoParametersConditions):
            if("canp" in palabra.lower()):                                                  
                listTokens.append("TwoParametersCondition(n,X)")                            
            elif ("canmovein" in palabra.lower()) or ("canjumpin" in palabra.lower()):                  
                listTokens.append("TwoParametersCondition(n,D)")                
            else:               
                listTokens.append("TwoParametersCondition(n,O)")   

        elif (palabra.lower() in singleParameterConditions):
             if("facing" in palabra.lower()):
                listTokens.append("SingleParameterCondition(D)")
             if("not" in palabra.lower()):
                listTokens.append("SingleParameterCondition(cond)")

        elif (palabra.lower() in listPROCS):
            listTokens.append("F({})".format(palabra.lower()))

        elif (palabra in specialCharacters):
            listTokens.append(palabra) 
        
        elif (palabra.lower() in directions):
            listTokens.append("D")

        elif (palabra.lower() in orientations):
            listTokens.append("O")

        elif (palabra.lower() == "nop"):
            listTokens.append(palabra)

        elif(palabra.lower() in chipsOrballons):
            listTokens.append("X")
        
        elif (palabra.isnumeric()):
            listTokens.append("#")

        
        else:
            nombres = definirNombresdeVariables(palabra)
            for nombre in nombres:
                if (nombre not in specialCharacters) and (nombre.upper() not in starters) and (nombre.lower() not in conditionals) and (nombre.lower() not in loop) and (nombre.lower() not in twoParametersCommands) and (nombre.lower() not in twoParametersConditions) and (nombre.lower() not in singleParameterCommands) and (nombre.lower() not in singleParameterConditions) and (nombre.isnumeric() == False) and (palabra.lower() not in chipsOrballons):
                    listTokens.append("n({})".format(nombre))
                else:
                    convertirATokens([nombre], listTokens, listPROCS)


def crearListaPalabras(archivo: str):
    strLineas = ""
    listPalabras = []
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
    
    file.close()
    
    return listPalabras

    

def lexer(archivo: str):
    listTokens = []
    listPalabras = crearListaPalabras(archivo)

    listaPROCS = definirNombresPROCS(listPalabras)

    convertirATokens(listPalabras, listTokens,listaPROCS)
    strTokens = " ".join(listTokens)


    print(strTokens)
    print(listaPROCS)
    lexertxt = open(archivo + "_lexer{0}.txt".format(random.randint(0, 1000)), "x")

    lexertxt.write(strTokens)

    lexertxt.close()

lexer("archivo")