archivoTokens = "ROBOT_R VARS Name , Name , Name , Name ; PROCS Name [ | Name , Name | TwoParametersCommand : Name , Name ; TwoParametersCommand : Name , Name ; TwoParametersCommand : Name , Name ] Name [ | | WHILE : TwoParametersCondition : Name , Name Name : [ TwoParametersCommand : Name , Name ] Name ] Name [ | | IF : TwoParametersCondition : Name , Name Name : [ TwoParametersCommand : Name , Name ] ELSE : Name : ] [ TwoParametersCommand : Name , Name Name : Name , Name ]"
archivoTokensLista = archivoTokens.split()
def isValid(test_str):
    
  """Verifica si una cadena tiene los parentesis, corchetes bien puestos.

  Args:
    test_str (str): The parentheses string to be validated
  
  Returns:
    True if test_str is valid; else False 
  """
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


def filterP(archivoTokensLista: str):
    test_str = []
    for i in range(0, len(archivoTokens)):
        if archivoTokens[i] == "(" or archivoTokens[i] == ")" or archivoTokens[i] == "[" or archivoTokens[i] == "]" or archivoTokens[i] == "{" or archivoTokens[i] == "}":
            test_str.append(archivoTokens[i]) 
    print(filterP)


def parser(archivo: str):
    filterLista = filterP(archivoTokensLista)
    filterStr = "".join(filterLista)
    if isValid(filterStr) == True:
        print("El programa tiene parentesis y corchetes válidos")
        #if x == None:
        #    Aa
    else:
        print("Las llaves, corchetes cuadrados o parentesis se encuentran mal, REVISE")

print(parser(archivoTokens))
