import Lexer

archivoTokens = "ROBOT_R VARS n(nom) , n(x) , n(y) , n(one) ; PROCS F(putcb) [ | n(c) , n(b) | TwoParametersCommand(#,n) : # , n(one) ; TwoParametersCommand(n,X) : n(c) , X ; TwoParametersCommand(n,X) : n(b) , X ] F(gonorth) [ | | WHILE : TwoParametersCondition(n,O) : # , D DO : [ TwoParametersCommand(n,D) : # , D ] ] F(gowest) [ | | IF : TwoParametersCondition(n,D) : # , D THEN : [ TwoParametersCommand(n,D) : # , D ] ELSE : nop : ] [ TwoParametersCommand(n,n) : # , # F(putcb) : # , # ]"

archivoTokensLista = archivoTokens.split()

def validCommandCall(command: str):
    """Funcion que recibe un string con el comando separado por : de los atributos que recibe.
    Retorna True si los atributos corresponden a los que deberia recibir, retorna False de lo contrario"""
    commandStr = command.replace(" ", "") 
    listCommand = commandStr.split(":")

    if (len(listCommand) != 2):
      return False

    commandType = listCommand[0]
    listAtributes = listCommand[1].split(",")

    # Para los verificar si los TwoParametersCommands reciben los parametros correctos en cualquier caso 
    if (commandType == "TwoParametersCommand(n,X)"):
      if ("n(" in listAtributes[0]) and (listAtributes[1] == "X"):
        return True
      else:
        return False
    
    if (commandType == "TwoParametersCommand(n,O)"):
      if ("n(" in listAtributes[0]) and (listAtributes[1] == "O"):
        return True
      else:
        return False

    if (commandType == "TwoParametersCommand(n,n)"):
      if ("n(" in listAtributes[0]) and ("n(" in listAtributes[1]):
        return True
      else:
        return False
    
    if (commandType == "TwoParametersCommand(#,n)"):
      if (listAtributes[0] == "#") and ("n(" in listAtributes[1]):
        return True
      else:
        return False

    if (commandType == "TwoParametersCommand(n,D)"):
      if ("n(" in listAtributes[0]) and (listAtributes[1] == "D"):
        return True
      else:
        return False

    # Para verificar que los SingleParameterCommands reciban el parametro correcto en cualquier caso
    if (commandType == "SingleParameterCommand(n)"):
      if ("n(" in listAtributes[0]):
        return True
      else:
        return False
    
    if (commandType == "SingleParameterCommand(O)"):
      if (listAtributes[0] == "O"):
        return True
      else:
        return False

    if (commandType == "SingleParameterCommand(D)"):
      if (listAtributes[0] == "D"):
        return True
      else:
        return False
    

def posicionPROCS(cadenaTokenizada: str):
    listTokens = cadenaTokenizada.split()
    i = 0
    dictFunciones = {}
    posicionesFunciones = []

    while i <= len(listTokens)-1:
      if "F(" in listTokens[i] and (listTokens[i] not in dictFunciones.keys()):
        dictFunciones[listTokens[i]] = 0
        posicionesFunciones.append(i)
      i += 1
    
    return [dictFunciones, posicionesFunciones]

def definirNumVariablesDePROC(cadenaTokenizada: str):
    listTokens = cadenaTokenizada.split()

    dictFunciones = posicionPROCS(cadenaTokenizada)[0]
    posicionesFunciones = posicionPROCS(cadenaTokenizada)[1]
    
    while i <= len(posicionesFunciones)-1:
      listaVariables = listTokens[posicionesFunciones[i]:-1]
      contadorLineas = 0
      index = 0

      while index <= len(listaVariables)-1:
        if listaVariables[index] == "|" and (contadorLineas < 2):
          contadorLineas +=1
        elif listaVariables[index] == "n":
          dictFunciones[listTokens[posicionesFunciones[i]]] += 1
        elif contadorLineas == 2:
            index = len(listaVariables)-1
        
        index += 1

      
      i += 1

      return dictFunciones

def pasarFuncionesaString(cadenaTokenizada: str):

    funciones = []
    subcadenas = []

    listTokens = cadenaTokenizada.split()
    posicionesFunciones = posicionPROCS(cadenaTokenizada)[1]

    for posicion in posicionesFunciones:
      subcadenas.append(listTokens[posicion+1: -1])
    
    i = 0

    for subcadena in subcadenas:
      inicio = 0
      final = 0

      cantAbierto = 0
      cantCerrado = 0

      i = 0
      while i <= len(subcadena)-1:
        if subcadena[i] == "[":
          cantAbierto += 1
        elif subcadena[i] == "]":
          cantCerrado += 1
          final = i

        if cantAbierto == cantCerrado:
          funcion = subcadena[inicio: final+1]
          funcion = " ".join(funcion)
          funciones.append(funcion)
          
          i = len(subcadena)-1
         
        i += 1

    return (funciones) 
     

def validPROCS(cadenaTokenizada: str):
    listTokens = cadenaTokenizada.split()
    posicionesFunciones = posicionPROCS(cadenaTokenizada)[1]

    if listTokens[posicionesFunciones[0]-1] != "PROCS":
      return False

    

def validarVariables(cadena: str):
    listaVariables = cadena.split(",")
    retorno = True

    for var in listaVariables:
      if ("n(" in var):                # Si el token que representa las variables no es n o #, las variables estan mal
        if (var != "#"):               # declaradas
          retorno = False
  
    return retorno

def validStart(cadenaTokenizada: str):
    """Verifica el inicio del archivo tokenizado, es decir, que inicie con ROBOT_R seguido de VARS con las variables
    y le siga la palabra PROCS. Retorna True si se cumplen las condiciones anteriores, False de lo contrario"""
  
    listTokens = cadenaTokenizada.split() 

    if (listTokens[0] != "ROBOT_R"):              # Si no inicia con ROBOT_R el archivo esta mal escrito
      return False
  
    elif (listTokens[1] != "VARS"):               # Si a ROBOT_R no le sigue la palabra VARS el archivo esta mal escrito
      return False

    else:
      i = 0
      indexPuntoYComa = 0       # Posicion en donde esta el punto y coma que marca el final de la declaracion de variables

      while i <= len(listTokens)-1:
        if listTokens[i] == ";":                # Determina la posicion en donde esta el ;   
          indexPuntoYComa = i                 
          i = len(listTokens)
        i += 1
    
      else:
        cadenaVariables = "".join(listTokens[2:indexPuntoYComa])
        if (validarVariables(cadenaVariables) == False):
          return False
        else:
          if (listTokens[indexPuntoYComa+1] != "PROCS"):  # Si la palabra despues del ; de la declaracion de variables 
            return False                                  # no es PROCS el archivo esta mal escrito
          else:
            return True


def validParentesis(cadenaTokenizada: str):
  
      
    """Verifica si una cadena tokenizada tiene los parentesis, corchetes bien puestos.
  
    Args:
      test_str (str): La cadena a ser validada
    
    Returns:
      True si test_str es válido; else False 
    """
    list = cadenaTokenizada.split()
    parentList = ["(",")","[","]","{","}"]
    filterList = []
    for char in list:
     if char in parentList:
       filterList.append(char)
  
    test_str = "".join(filterList)
    #print(test_str)
    # si la longitud es impar -> invalida!
    if len(test_str)%2 != 0:
      return False
    # initialize parentheses dict
    par_dict = {'(':')','{':'}','[':']'}
    stack = []
    for char in test_str:
      # push opening bracket to stack
      if char in par_dict.keys():
        stack.append(char)
      else:
        # closing bracket without matching opening bracket
        if stack == []:
            return False
        # if closing bracket -> pop stack top
        open_brac = stack.pop()
        # not matching bracket -> invalid!
        if char != par_dict[open_brac]:
          return False
    return stack == []  


def parser(archivoTokenizado: str):
    if (validParentesis(archivoTokenizado) == True):
      print("El programa tiene parentesis y corchetes válidos")
      
    else:
        print("Las llaves, corchetes cuadrados o parentesis se encuentran mal, por favor REVISE los mismos")
    
    if ((validStart(archivoTokenizado) == True)):
      print("El programa tiene un inicio valido")
    else:
      print("El programa presenta alguna inconcistencia en el inicio")


print(parser(archivoTokens))