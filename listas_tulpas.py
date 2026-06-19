nome_lista = ["distribuição conjunta e distribuições marginais", "distribuição normal", "função de densidade e probabilidade", "variavel discreta",  "função deprobabilidade", "variaveis continuas", "correlação", "distribuição de poisson", "distribuição de probabilidade", "distribuição binomial", "distribuição de Bernoulli"]

dia = 1
for i in range(1, len(nome_lista)-1, 2):
        print(f"{dia}º dia:\n {i}. {nome_lista[i]}\n {i+1}. {nome_lista[i+1]}\n")
        dia += 1

temas_por_dia = len(nome_lista)/8
