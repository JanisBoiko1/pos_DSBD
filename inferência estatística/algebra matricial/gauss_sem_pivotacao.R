# obter a matriz triangular superior
gauss <- function(A, b) {
  Ae <- cbind(A, b) ## Sistema aumentado
  rownames(Ae) <- paste0("x", 1:length(b))
  n_row <- nrow(Ae)
  n_col <- ncol(Ae)
  SOL <- matrix(NA, n_row, n_col) ## Matriz para receber os resultados
  SOL[1,] <- Ae[1,]
  pivo <- matrix(0, n_col, n_row)
  for(j in 1:c(n_row-1)) {
    for(i in c(j+1):c(n_row)) {
      pivo[i,j] <- Ae[i,j]/SOL[j,j]
      SOL[i,] <- Ae[i,] - pivo[i,j]*SOL[j,]
      Ae[i,] <- SOL[i,]
    }
  }
  return(SOL)
}

#substituição regressiva
sub_reg <- function(SOL) {
  n_row <- nrow(SOL)
  n_col <- ncol(SOL)
  A <- SOL[1:n_row,1:n_row]
  b <- SOL[,n_col]
  n <- length(b)
  x <- c()
  x[n] <- b[n]/A[n,n]
  for(i in (n-1):1) {
    x[i] <- (b[i] - sum(A[i,c(i+1):n]*x[c(i+1):n] ))/A[i,i]
  }
  return(x)
}

#definir matriz A
A <- matrix(c(1.0,0.4,0.4,0.3,0.4,1.0,0.3,0.4,0.4,0.3,1.0,0.4,0.3,0.4,0.4,1.0),4,4)

# definir vetor b
b <- c(5,12,9,12)

## Passo 1: Triangularização
S <- gauss(A, b) 

## Passo 2: Substituição regressiva
sol = round(sub_reg(SOL = S), 3)
sol
