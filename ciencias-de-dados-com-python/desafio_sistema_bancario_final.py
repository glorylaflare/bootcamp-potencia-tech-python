def menu():
    menu = """
    ====================== MENU DE OPÇÕES - BANCO DA SORTE ======================

    [1] Depositar um valor
    [2] Sacar um valor
    [3] Verificar seu extrato
    [4] Criar uma nova conta
    [5] Listar contas
    [6] Novo usuário
    [0] Sair
    
    Digite uma das opções acima: """
    
    return input(menu)

def depositar(saldo, deposito, extrato, /):
    if deposito < 0:
        print("/!\/!\/!\ A OPERAÇÃO FALHOU! /!\/!\/!\ \nVocê inseriu um valor inválido.")
    else:
        saldo += deposito
        extrato += f"Depósito : R$ {deposito:.2f}\n"
        print("Operação concluída com sucesso!")
    
    return saldo, extrato
    
def sacar(*, saldo, extrato, limite, numero_saques, limite_saques):
    if numero_saques == limite_saques:
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
    
    return saldo, extrato
        
def exibir_extrato(saldo, /, *, extrato):
    print("########## EXTRATO ##########")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"Saldo R$ {saldo:.2f}")
    print("#############################")
    
def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente numero): ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return
    
    nome = input("Informe seu nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, numero - bairro - cidade/estado): ")
    
    usuario.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereço": endereco})
    print("////// Usuário criado com sucesso! //////")
    
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None
    
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF (somente numero): ")
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("\n////// Conta criada com sucesso! //////")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")
    
def listar_conta(contas):
    for conta in contas:
        linha = f"""
        Agência: {conta['agencia']}
        C/C: {conta['numero_conta']}
        Titular: {conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)
    
def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()
        if opcao == "1":
            deposito = float(input("Qual quantia você deseja depositar: "))
            
            deposito, extrato = depositar(saldo, deposito, extrato)                
        elif opcao == "2":
            saldo, extrato = sacar(saldo=saldo, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES,)
                                    
        elif opcao == "3": 
            exibir_extrato(saldo, extrato=extrato)
            
        elif opcao == "4": 
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            
        elif opcao == "5": 
            listar_conta(contas)
            
        elif opcao == "6": 
            criar_usuario(usuarios)
            
        elif opcao == "0":
            print("Obrigado por utilizar nossos serviços, a operação foi encerrada!")
            break
        
        else:
            print("Operação inválida, por favor seleciona novamente a opção desejada.")

main()