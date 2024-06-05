print("Seja bem-vindo ao seu Sistema Bancário! Selecione a opção desejada de acordo com o menu.")

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    print("MENU DE OPÇÕES:")
    print("[1] - Depositar")
    print("[2] - Sacar ")
    print("[3] - Extrato")
    print("[4] - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        valor = float(input("Informe o valor que deseja depositar: "))

        if valor > 0:
            saldo += valor
            print("Depósito realizado com sucesso!")
            extrato += f"Depósito: R$ {valor:.2f}\n"
            

        else:
            print("Valor Inválido.")

    elif opcao == "2":
        valor = float(input("Informe o valor que deseja sacar: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Você não possui saldo suficiente para realizar essa operação.")

        elif excedeu_limite:
            print("O valor que deseja sacar excede o limite de saque.")

        elif excedeu_saques:
            print("Número máximo de saques excedido!")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso!")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "4":
        print("Saindo...")
        break

    else:
        print("Operação Inválida! Por favor, selecione novamente a operação desejada.")
        

    repetir = input("Deseja continuar? s/n: ")
    if repetir == "n":
        print("Saindo...")
        break