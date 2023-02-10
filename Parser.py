archivoTokens = "ROBOT_R VARS Name , Name , Name , Name ; PROCS Name [ | Name , Name | TwoParametersCommand : Name , Name ; TwoParametersCommand : Name , Name ; TwoParametersCommand : Name , Name ] Name [ | | WHILE : TwoParametersCondition : Name , Name Name : [ TwoParametersCommand : Name , Name ] Name ] Name [ | | IF : TwoParametersCondition : Name , Name Name : [ TwoParametersCommand : Name , Name ] ELSE : Name : ] [ TwoParametersCommand : Name , Name Name : Name , Name ]"

archivoTokensLista = archivoTokens.split()

def isValid(cadenaTokenizada):

    
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


def parser(archivoTokenizado):
    if isValid(archivoTokenizado) == True:
      print("El programa tiene parentesis y corchetes válidos")
      
    else:
        print("Las llaves, corchetes cuadrados o parentesis se encuentran mal, por favor REVISE los mis")


print(parser(archivoTokens))