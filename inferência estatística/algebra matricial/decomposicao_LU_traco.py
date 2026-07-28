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

#definir matriz A
A = np.array([
    [1.0,0.8,0.8,0.7],
    [0.8,1.0,0.7,0.8],
    [0.8,0.7,1.0,0.8],
    [0.7,0.8,0.8,1.0]
])

#chamar funcao
L, U = decomposicao_LU(A)
print(L)
print(U)

#calcular o traço de U
traco = sum(np.diag(U))
print()
print(traco)

