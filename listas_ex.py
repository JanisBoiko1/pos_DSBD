import random

## EX 01
soma = [1,2]
for i in range(0,7):
    novo = sum(soma)
    soma.append(novo)
    
#print(soma)

## EX 02
lista = [random.randint(1, 100) for i in range(10)]
print(lista)
lista.sort()
print(lista)

print(lista[0])
print(lista[9])
    
## EX 04
i = len(lista)
nova_lista = []
for i in range(len(lista)-1, 0, -1):
    nova_lista.append(lista[i])

print(nova_lista)

## EX 05
for i in range(0, len(lista)-2):
    if(lista[i] == lista[i+1]):
        print(f"Há duplicatas!\n{i}. {lista[i]} e {i+1}. {lista[i+1]}")
        lista.pop(i+1)
        
print(f"Nova lista:{lista}")

##EX 06
print("\n\n")
lista_1 = [random.randint(1, 100) for i in range(10)]
lista_2 = [random.randint(1, 100) for i in range(10)]

print(lista_1)
print(lista_2)

mesclada = []

for i in range(0, len(lista_1)):
    mesclada.append(lista_1[i])
    mesclada.append(lista_2[i])

print("\n")
print(mesclada)

##EX 07
print("\n\n")
rotacionada = []
print(lista_1)
print("\n")

for i in range(0, len(lista_1), 2):
    sublista1=[]
    sublista2=[]
    sublista1.append(lista_1[i+1])
    sublista1.append(lista_1[i])
    sublista2.append(lista_1[i+3])
    sublista2.append(lista_1[i+2])
    rotacionada.append(sublista1)
    rotacionada.append(sublista2)

print(rotacionada)