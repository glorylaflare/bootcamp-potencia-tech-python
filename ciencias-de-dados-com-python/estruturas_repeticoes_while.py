opcao = -1

while opcao != 0:
    opcao = int(input("1 para sacar,\n2 para extrato\n0 para sair\n: "))
    
    if opcao == 1:
        print("sacando...")
    elif opcao == 2:
        print("exibindo o extrato...")
else:
    print("Obrigado por usar nosso sistema bancário, até logo!")