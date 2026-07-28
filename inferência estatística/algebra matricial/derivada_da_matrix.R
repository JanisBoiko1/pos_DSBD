# Código Lucio
I <- matrix(c(1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1), nrow = 4, byrow = TRUE)
print(I)

cat('\n','Matriz Z:','\n')
Z <- matrix(c(1,1,0,0,1,1,0,0,0,0,1,1,0,0,1,1), nrow = 4, byrow = TRUE)
print(Z)

tau0 <- 2
tau1 <- 1

#multiplicação por escalar de tau pelas matrizes compõe A
A <- tau0 * I + tau1 * Z

#multiplicação de A por z, calculo da diagonal do produto e soma dos ítens da diagonal
resultado <- sum(diag(solve(A) %*% Z))
print(resultado)

