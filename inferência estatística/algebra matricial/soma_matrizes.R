#Definir matriz A e B
A <- matrix(c(9,10,11,5,11,9,10,10,12,9,5,13,9,7,6,10,18,12,4,9,19,7,15,15,7), nrow = 5, ncol = 5)
B <- matrix(c(11,10,3,9,8,4,9,11,5,7,12,6,10,11,9,9,9,13,9,9,10,11,4,16,11), nrow = 5, ncol = 5)

#somar matrizes
C <- A+B
print(C)

#somar matrizes
soma_total <- sum(C)
print(soma_total)
