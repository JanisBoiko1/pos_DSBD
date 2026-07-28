A <- matrix(c(8,10,9,8,6,9,8,5,10,6,5,6,8,12,11,8,8,13,11,7),4,5)
print(A)

#checa se a matriz é simetrica
isSymmetric.matrix(A)

#fornece a decomposição
#valotes singulares em $d
print(svd(A))

