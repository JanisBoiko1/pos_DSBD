#determinar A
A <- matrix(c(1.00,0.47,0.47,0.34,0.47,1.00,0.34,0.47,0.47,0.34,1.00,0.47,0.34,0.47,0.47,1.00), nrow = 4, ncol = 4)

#calcular inversa de A
A_inv <- solve(A)
print(A_inv)

#determinante da inversa
determinante <- det(A_inv)
print(round(determinante,3))

#traço da inversa
traco <- sum(diag(A_inv))
print(round(traco, 3))
