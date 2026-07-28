#funcao jacobiana
#recebe a matriz e o vetor, um valor inicial a ser atribuido
#numero maximo de iterações e a tolerância para o critériode parada
gauss_seidel <- function(A, b, inicial, max_iter = 10, tol = 1e-04) {
  
  #n guarda o tamanho do vetor
  n <- length(b)
  
  #cria uma matriz temporaria vazia e joga nela o chute inicial
  x_temp <- matrix(NA, ncol = n, nrow = max_iter)
  x_temp[1,] <- inicial
  x <- x_temp[1,]
  
  #loop pela matriz calculando a formula atualizando a matriz A
  for(j in 2:max_iter) { 
    for(i in 1:n) {
      
      # pegar cada elemento da linha i da matriz e cada elemento 
      # do vetor x, multiplica e soma, subtrai b[i]
      # e divide pelo valor original que tinhamos nessa posição na
      # matriz A
      ## DIFERENÇA COM JACOBIANO SERIA QUE PODE ATUALIZARI DIRETO
      ## NA MATRIZ 
      x[i] <- (b[i] - sum(A[i,1:n][-i]*x[-i]))/A[i,i]
    }
    
    # salva a solção dessa iteração
    x_temp[j,] <- x
    
    # calcula a diferenca entre a solução atual e anterior, e se 
    # for menos que o tol, sai do loop
    if(sum(abs(x_temp[j,] - x_temp[j-1,])) < tol) break 
  }
  return(list("Solucao" = x, "Iteracoes" = x_temp))
}

#cria a matriz
A <- matrix(c(2.5,0.8,0.8,0.8,0.8,2.5,0.8,0.8,0.8,0.8,2.5,0.8,0.8,0.8,0.8,2.5),4,4)
# cria o vetor
b <- c(11,5,11,11)
#chama a funçao
ss <- gauss_seidel(A = A, b = b,
             inicial = c(0,0,0,0),
             max_iter = 50)
## Solução aproximada
ss$Solucao
## print numero de iterações
iteracoes_feitas <- sum(!is.na(ss$Iteracoes[,1]))
print(iteracoes_feitas)

