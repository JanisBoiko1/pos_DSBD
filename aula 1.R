#instala o pacote
#library(ggplot2)

#mostra o pacote em si
#ls("package:ggplot2")

#abre o help de todo o pacote
help(package = "ggplot2")
#?mean
.libPaths()

#remover pacote
# detach("package:ggplot2", unload = TRUE)

#chamar o pacote
#ggplot2::ggplot()

??mean
help.search("mean")
#encontra funções com nome "mean"
apropos("mean")

#nomeando variáveis em R
#_ ou camel case
#evitar chamar de "c" variáveis

x = 5

y = 10

z = x + y

if (x == y)