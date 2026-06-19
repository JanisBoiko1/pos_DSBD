opcao = input("Forma de pagamento [c|d|b|o]: ")

if (opcao == 'c'):
    print("Pagamento no credito sem desconto.")
elif (opcao =='d'):
    print("Pagamento no débito com 3% de desconto.")
elif (opcao == 'b'):
    print("Pagamento no boleto com 5% de desconto.")
elif (opcao == 'o'):
    print("Pagamento em dinheiro com 10% de desconto.")
else:
    print("Opção '{}' não cadastrada".format(opcao))
    opcao = input("Forma de pagamento [c|d|b|o]: ")


