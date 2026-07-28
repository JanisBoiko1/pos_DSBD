import numpy as np

#calcula o determinante da matriz quadrada fornecida
#np.linalg.det(array)

#calcula os autovetores e autovalores de uma matriz quadrada
#np.linalg.eig()

#extrai e constrói uma matriz Diagonal
#np.diag(autovalores)

A = np.array([
    [2, 1, 1],
    [1, 3, 2],
    [1, 2, 4]
])

determinante = np.linalg.det(A)
print(determinante)

if not np.isclose(determinante, 0):
    autovalores, autovetores = np.linalg.eig(A)

    #colocando os autovalores em ordem decrescente
    posicao = np.argsort(autovalores)[::-1]
    autovalores_ordenados = autovalores[posicao]
    autovetores_ordenados = autovetores[:, posicao]

    #calcula a matriz de diagonal de autovalores
    matrizDiagonal = np.diag(autovalores_ordenados)
    
    print("\nOs autovalores são:\n\n{}\n\n".format(autovalores))
    print("\nA Matriz Diagonal de autovalores:\n\n{}\n\n".format(matrizDiagonal))
    print("\nOs autovetores são:\n{}".format(autovetores))
else:
    print("ERRO!")