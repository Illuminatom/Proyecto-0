### import numpy as np // USO DE MATRICES PARA MODELAR CAMINO 
#INPUT EJEMPLO#
print("Hola, Bienvenido al programa para validar las lineas \ndel tipo -INPUT- para el robot\n")
line = input("Ingrese la linea de comandos para el robot: \n") 
#Exam: R;M;R;B;M;J(5);C;G(7,1);
lineList = line.split(";")
i=0
emptyLineList = ['']
"""if len(lineList) == 1:
      print("Entra caso de longitud 1")
      print(len(lineList))
      if (lineList[i] == " ") or (lineList[i] == "") or (lineList[i] == "\n"):
        print(lineList,lineList[i])
        print("Para dejar vacia")
        lineList = []"""
if len(lineList) >= 2:
    while i < len(lineList):
      print(len(lineList))
      ###
      if len(lineList) == 1:
        print("Entra caso de longitud 1")
        print(len(lineList))
      
        if (lineList[i] == " ") or (lineList[i] == "") or (lineList[i] == "\n"):
          print(lineList,lineList[i])
          print("Para dejar vacia")
          lineList = []
          break
      ###
      if (lineList[i] == " ") or (lineList[i] == "") or (lineList[i] == "\n"):
        print(lineList,lineList[i])
        print("Para borrar")
        lineList[i] = lineList.pop()
      else:
        lineList[i] = lineList[i].upper()
        print("Se mantiene")
        i += 1
else:
  print(lineList, len(lineList))
  print(lineList)
print("Los datos filtrados y organizados en un solo estandar son los siguientes: \n" + str(lineList) + "\n")
print("Comienza la lectura de datos...") 

print(lineList)
#def LexerP0 (lineSplit):
#  for i in range(0, len(lineList)):
#    if lineList[i] == 