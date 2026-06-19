import pandas as pd

lista = [-5, 0, 8, -12, 100, 33, 7, -1, 1, 2]

serie = pd.Series(lista)
valor = serie.values
tipo = type(serie.values)
indice = serie.index
print(serie)
print(valor)
print(tipo)
print(indice)