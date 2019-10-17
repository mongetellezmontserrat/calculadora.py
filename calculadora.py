def calc(numero1, operando, numero2):
     if operando == "suma":
          return suma(numero1, numero2)
     elif  operando == "resta":
          return resta(numero1, numero2)
     elif operando == "division":
          return div(numero1, numero2)
     elif operando == "multiplicacion":
          return mult(numero1, numero2)
     elif operando == "factorial":
          return facto(numero1, numero2)
     elif operando == "sumatoria":
          return sumatoria(numero1, numero2)


def suma(numero1, numero2):
     sumas=numero1+numero2
     return sumas

def resta(numero1, numero2):
     restas=numero1-numero2
     return restas
def div(numero1, numero2):
     division=numero1/numero2
     return division

def mult(numero1, numero2):
     multiplicacion=numero1*numero2
     return multiplicacion

def facto(numero1):
     if numero1 == 0 or numero1 == 1:
          return  1
     elif numero1>1:
          return numero1*facto(numero1)
def  sumatoria(numero1, numero2):
     if numero1 >= 0 and numero1 <= 20 and numero2 <= 0 and numero2 >= 20:
          return 0
     else:
          return sumatoria(numero1-1, numero2-2)
     
