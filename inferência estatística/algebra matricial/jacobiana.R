#funcao jacobiana
#recebe a matriz e o vetor, um valor inicial a ser atribuido
#numero maximo de iterações e a tolerância para o critériode parada
jacobi <- function(A, b, inicial, max_iter = 10, tol = 1e-04) {
  
  #n guarda o tamanho do vetor
  n <- length(b)
  
  #cria uma matriz temporaria vazia e joga nela o chute inicial
  x_temp <- matrix(NA, ncol = n, nrow = max_iter)
  x_temp[1,] <- inicial
  x <- x_temp[1,]
  
  #loop pela matriz calculando a formula atualizando a matrizA
  for(j in 2:max_iter) {
    for(i in 1:n) {
      
      # pegar cada elemento da linha i da matriz e cada elemento 
      # do vetor x, multiplica e soma, subtrai b[i]
      # e divide pelo valor original que tinhamos nessa posição na
      # matriz A
      x_temp[j,i] <- (b[i] - sum(A[i,1:n][-i]*x[-i]))/A[i,i]
    }
    
    #atualiza o valor em x
    x <- x_temp[j,]
    
    # calcula a diferenca entre a solução atual e anterior, e se 
    # for menos que o tol, sai do loop
    if(sum(abs(x_temp[j,] - x_temp[c(j-1),])) < tol) break 
  }
  return(list("Solucao" = x, "Iteracoes" = x_temp))
}

#cria a matriz
A <- matrix(c(2.5,0.8,0.8,0.8,0.8,2.5,0.8,0.8,0.8,0.8,2.5,0.8,0.8,0.8,0.8,2.5),4,4)
# cria o vetor
b <- c(11, 10, 5, 14)
#chama a funçao
ss <- jacobi(A = A, b = b,
             inicial = c(0,0,0,0),
             max_iter = 1000)
## Solução aproximada
ss$Solucao
## print numero de iterações
iteracoes_feitas <- sum(!is.na(ss$Iteracoes[,1]))
print(iteracoes_feitas)

