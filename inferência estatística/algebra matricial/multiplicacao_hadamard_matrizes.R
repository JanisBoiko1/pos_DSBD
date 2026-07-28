#Definir matriz A e B
A <- matrix(c(15,10,7,10,6,13,10,7,12,10,14,11,7,5,3,4,12,11,8,7,6,9,10,15,5), nrow = 5, ncol = 5)
B <- matrix(c(5,8,11,9,14,14,16,11,11,8,14,10,10,14,6,6,12,15,11,9,9,4,9,17,13), nrow = 5, ncol = 5)

#multiplicar matrizes (hadamard)
C <- A*B
print(C)

#somar matriz
soma_total <- sum(C)
print(soma_total)

