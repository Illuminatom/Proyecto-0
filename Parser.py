import Lexer

archivoTokens = "ROBOT_R VARS n , n , n , n ; PROCS F(putcb) [ | n , n | TwoParametersCommand(#,n) : # , n ; TwoParametersCommand(n,X) : n , X ; TwoParametersCommand(n,X): n , n ] F(gonorth) [ | | WHILE : TwoParametersCondition(n,O) : # , D DO : [ TwoParametersCommand(n,D) : # , D ] n ] F(gowest) [ | | IF : TwoParametersCondition(n,D) : # , D THEN : [ TwoParametersCommand(n,D) : # , D ] ELSE : nop : ] [ TwoParametersCommand(n,n) : # , # F(putcb) : # , n ]"

archivoTokensLista = archivoTokens.split()

def validarVariables(cadena: str):
    listaVariables = cadena.split(",")
    retorno = True

    for var in listaVariables:
      if (var != "n"):                # Si el token que representa las variables no es n o #, las variables estan mal
        if (var != "#"):              # declaradas
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