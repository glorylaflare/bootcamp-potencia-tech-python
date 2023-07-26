menu_mensagem = """
###### MENU DE OPÇÕES - BANCO X ######

[1] Depositar um valor
[2] Sacar um valor
[3] Verificar seu extrato

[0] Sair

Digite uma das opções acima: """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu_mensagem)
    if opcao == "1":
        deposito = float(input("Qual quantia você deseja depositar: "))
        if deposito < 0:
            print("Você inseriu um valor inválida, por favor insira um valor positivo")
        else:
            saldo += deposito
            extrato += f"Depósito : R$ {deposito:.2f}\n"
            print("Operação concluída com sucesso!")
            
    elif opcao == "2":
        if numero_saques == LIMITE_SAQUES:
            print("Você atingiu seu limite de saques diários!")
        else:
            saque = float(input(f"Qual quantia você deseja sacar:\nVocê ainda tem {3 - numero_saques} disponíveis.\n"))
            
            if saque > limite or saque < 0:
                print("Você inseriu um valor inválida, por favor insira um valor entre 0 e 500")
            elif saque > saldo:
                print("Você não tem saldo suficiente para sacar")
            else:
                saldo -= saque
                extrato += f"Saque: R$ {saque:.2f}\n"
                numero_saques += 1
                print("Operação concluída com sucesso!")
                
    elif opcao == "3":        
        print("########## EXTRATO ##########")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo R$ {saldo:.2f}")
        print("#############################")
        
    elif opcao == "0":
        print("Obrigado por utilizar nossos serviços, a operação foi encerrada!")
        break
    
    else:
        print("Operação inválida, por favor seleciona novamente a opção desejada.")