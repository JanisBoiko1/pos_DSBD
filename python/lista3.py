import pandas as pd
import seaborn as sns

# Carregar um arquivo CSV local
df = pd.read_csv('trainTitanic.csv')

# Visualizar as primeiras 5 linhas
print(df.head())

#selecionar todos os mortos cuja coluna Pclass == 3
#df.loc[(df['pclass'] == 3) & (df['survived'] == 0)]
mortos_3_classe = df[(df['Pclass'] == 3) & (df['Survived'] == 0)].shape[0]

print(f"Mortos de 3ª classe: {mortos_3_classe}")

#Fare mais alta
maior_fare = df['Fare'].max()
print(f"A passagem mais cara custou ${maior_fare}")

#boxplot
plotbox = sns.boxplot(df)
figbox = plotbox.get_figure()
figbox.savefig("box1.jpg")

#pessoa mais jovem no df
passageiro_mais_jovem = df['Age'].min()
print(f"A idade do passageiro mais jovem a bordo do Titanic é: {passageiro_mais_jovem}")