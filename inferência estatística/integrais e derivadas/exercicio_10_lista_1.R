# Passo 1: criar vetor x de -3 a 3 com muitos pontos
x = seq(-3, 3, length.out = 1000)

# Passo 2: calcular y para cada x usando ifelse (funciona vetorizado)
y = ifelse(abs(x) >= 1, 1/x^2, 2)

# Passo 3: plotar
plot(x, y, type = "l", ylim = c(0, 3), 
     xlab = "x", ylab = "f(x)", main = "Gráfico de f(x)")

# Passo 4: adicionar linhas verticais pontilhadas
abline(v = c(-1, 1), lty = 2, col = "gray")

# Passo 5: marcar os pontos de descontinuidade
# A função vale 1 em x = -1 e x = 1
points(c(-1, 1), c(1, 1), pch = 19, col = "black")
# Limites laterais (valor 2) como círculos abertos
points(c(-1, 1), c(2, 2), pch = 1, col = "black")

