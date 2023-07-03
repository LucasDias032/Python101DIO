import datetime


#versao 1

opcao = -1
saldo = 1000.0
saque = 0.0
deposito = 0.0
data_atual = datetime.date.today()
saques_diarios = 0
limite_saques = 3
limite = 500.0
extrato = []

while opcao != 0:
    opcao = int(input("""
        ================ MENU ================
            Digite a operaçao desejada 
                [1] Sacar
                [2] Depositar
                [3] Extrato
                [0] Sair
         ======================================
    """))

    if opcao == 1:
        if saques_diarios < limite_saques:
            print(f"Seu saldo em conta e de R${saldo}")
            saque = float(input("Digite o valor desejado do saque:"))
            if saque > limite:
                print(f"""  Nao foi possível realizar o saque.\n   O Limite para essa conta é de R${limite}""")
            else:
                if saque > saldo:
                    print(f"Saldo insuficiente para saque. \n O saldo disponivel para saque e de R${saldo}")
                else:
                    print("    Saque realizado com sucesso!")
                    saldo -= saque
                    print(f"    Seu novo saldo e de R${saldo}")
                    extrato.append(f"Saque: R$ {saque: .2f} - Data: {data_atual}")
                    saques_diarios += 1

        else:
            print("Limite diario de saques excedido.")
    elif opcao == 2:
        print(f"Seu saldo em conta e de R${saldo}")
        deposito = float(input("Digite o valor desejado do deposito:"))
        if deposito > 0:
            saldo += deposito
            print(f"""  Deposito realizado com sucesso!\n  Novo valor em conta de {saldo}""")
            extrato.append(f"Depósito: R$ {deposito: .2f} - Data: {data_atual}")
        else:
            print("Digite um valor positivo para depositar")
    elif opcao == 3:
        print(f"""  ================ EXTRATO ================
    Data da consulta: {data_atual}
    Saldo em conta: {saldo}""")
        print(extrato, end="\n")
        print(" =========================================")
    else:
        print("Opçao Inválida")
else:
    print("Obrigado por usar o Banco LDIO")
