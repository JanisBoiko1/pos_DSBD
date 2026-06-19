import math 
import numpy as np

## Exericio 01
def baskara(a, b, c):

  delta = b**2-4*a*c
  x1_0 = (-(b)+math.sqrt(delta))/2*a
  x2_0 = (-(b)-math.sqrt(delta))/2*a
  x1_1 = np.round(x1_0, 3)
  x2_1 = np.round(x2_0, 3)
  return(x1_0, x2_0, x1_1, x2_1)

#x²-6x+5
print("x²-6x+5")
print(baskara(1, -6, 5))

## Exercicio 02
def cubica(x):
  y = x ** (1/3)
  return(y)

print("27")
print(cubica(27))

## Exercicio 03
def conta(a,b,c):
  y= a+b*c
  if (y != 1500):
    y = round((a*2.0375)+(b*2.0375)*(c*2.0375))
  return(y)

print("23+7*50")
print(conta(23,7,50))

def par_impar(x):
  y = x%2
  if(y==0):
    print(f"{x} é par!")
  else:
    print(f"{x} é ímpar!")
    
par_impar(6)

def area_circulo(raio):
  area = math.pi * pow(raio, 2)
  print(f"A área é: {round(area, 3)}")

area_circulo(5.0)

texto = "HAqui temos uma string"
novo = texto[0::3]
print(novo)

