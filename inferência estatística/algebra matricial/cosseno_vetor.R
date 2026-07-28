#Declare os vetores
a <- c(9,9,6,8,11)
b <- c(4,8,18,6,14)

#calculando cosseno
cos <- t(a)%*%b/(sqrt(t(a)%*%a)*sqrt(t(b)%*%b))

print(round(cos, 3))

