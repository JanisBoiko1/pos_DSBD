#Definir matriz A e B
A <- matrix(c(8,7,11,8,10,14,9,8,6,10,7,8,11,10,14,12,4,12,13,11,4,9,7,10,15), nrow = 5, ncol = 5)
B <- matrix(c(9,8,12,9,8,10,14,9,10,11,11,7,12,13,6,9,13,10,13,5,13,10,5,4,6), nrow = 5, ncol = 5)

#multiplicar matrizes
C <- A%*%B
print(C)

#somar matrizes
soma_total <- sum(C)
print(soma_total)
