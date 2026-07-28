
#funcao transformacao da matriz A em matriz identidade
def gauss_jordan(A,b):
    n = len(A)
    ## para cada etapa k
    for k in range(0, n):
        #para cada linha i
        #transformar o povô em 1
        #percorrer a linha inteira
        for j in range(k+1, n):
            #elemento j da coluna k dividido pelo pivô
            A[k][j] = A[k][j]/A[k][k]
        #vetor b, linha k, recebe seu próprio elemento dividido pelo pivô
        b[k] = b[k]/A[k][k]
        A[k][k] = 1

        #Para cada linha 1
        for i in range(0, n):
            #se eu não estiver na linha do pivô
            if i != k:
                ##calcular fator m 
                m = - A[i][k]/A[k][k]
                #atualizar a linha i da matriz, percorrendo todas as colunas j
                for j in range(k+1, n):
                    A[i][j] = m * A[k][j] + A[i][j]
                #atualizar o vetor b na linha i
                b[i] = m * b[k] + b[i]

                #zero o contador
                A[i][k] = 0

    return b

#definir matriz
A = [[2.0, 0.9, 0.9, 0.8],
     [0.9, 2.0, 0.8, 0.9],
     [0.9, 0.8, 2.0, 0.9],
     [0.8, 0.9, 0.9, 2.0],]
#definir vetor
b = [10, 8, 5, 9]
#chamar gauss_jordan
x = gauss_jordan(A, b)
print(x)
