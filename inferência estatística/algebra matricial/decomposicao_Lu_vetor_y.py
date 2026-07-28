import numpy as np

#funcao LU
def decomposicao_LU(A):
    A = A.astype(float)

    n = len(A)
    #cria uma matriz identidade L para base
    L = np.eye(n)
    
    #varre a matriz A
    for j in range(n-1):
        #calcula o pivô de A
        pivo = A[j, j]
        #varre as linhas abaixo do pivô
        for i in range (j+1, n):
            #calcula o fator
            fator = A[i,j]/pivo
            #Define L igual ao fator
            L[i,j] = fator
            #atualiza A com o valor menos o fator multiplicado pelo valor original
            A[i,:] = A[i,:] - fator*A[j, :]
        #matriz U é a propria matriz A
    U = A
    return(L, U)

def triangular_superior(U,y):
    n, nc = np.shape(U)
    x = np.zeros((n,1))
    for i in range (n-1, -1, -1):
        x[i,0] = ((y[i,0] - U[i,i:n]@x[i:n,0])/U[i,i])
    return(x)

def triangular_inferior(L,b):
    n, nc = np.shape(L)
    x = np.zeros((n,1))
    x[0,0]= b[0,0]/L[0,0]
    for i in range(1,n):
        x[i,0] = ((b[i,0] - L[i,0:i]@x[0:i,0])/L[i,i])
    return(x)

def metodo_LU(A,b):
    L, U = decomposicao_LU(A)
    y = triangular_inferior(L,b)
    x = triangular_superior(U,y)
    return(y)

#definir matriz A
A = np.array([
    [1.0,0.8,0.8,0.8],
    [0.8,1.0,0.8,0.8],
    [0.8,0.8,1.0,0.8],
    [0.8,0.8,0.8,1.0]
])

#definir vetor B
b = np.array([[12],[8],[7],[9]])

#chamar funcao
y = metodo_LU(A, b)
print(y)
print(sum(y))