
peso = 52
altura = 1.52

if (peso / altura**2 < 18.5):
    print("abaixo do peso")
    print(peso / altura**2)
elif (peso / altura**2 < 30):
    print("normal")
    print(peso / altura**2)
else:
    print("obesidade")
    print(peso / altura**2)
