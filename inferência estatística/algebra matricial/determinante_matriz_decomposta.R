autovalores = c(29.7,2.7,2.7,0.9)

#obter determinante
determinante = prod(autovalores)
print(determinante)

#obter log do determinante da inversa
log_det_inversa = -log(determinante)
print(round(log_det_inversa,3))

