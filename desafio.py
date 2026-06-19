texto = input("Digite um texto:")

print(len(texto))

contador_palavras = 1
for i in range(len(texto)):
    if(texto[i]==' '):
        contador_palavras +=1
    

print(contador_palavras)

maiusculas = ''
for i in range(len(texto)):
    if(texto[i].isupper()):
        maiusculas += texto[i]

print(maiusculas)