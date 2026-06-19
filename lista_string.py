#palavra = input("Digite sua palavra:")
#invertida = []

#for i in range(len(palavra)-1, -1, -1):
#    invertida.append(palavra[i])

#print("".join(invertida))


#frase = input("Digite uma frase:")
#contador = 0
#for i in range(len(frase)):

#    nova_frase = frase.lower()
#    #print(nova_frase)
#    if(frase[i] == 'a'or frase[i]=='e'or frase[i]=='i'or frase[i]=='o'or frase[i]=='u'):
#        contador += 1

#print(contador)

frase = input("Digite uma frase:")

def gerador_sigla(frase):
    sigla = ''
    for i in range(len(frase)):
        
        #check is upper:
        if(frase[i].isupper()):
            sigla += frase[i]
    
    return(sigla)

print(gerador_sigla(frase))

