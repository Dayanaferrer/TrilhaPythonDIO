menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

while True:
    opcao = input(menu)

    if opcao == '1':
        valor = float(input("Digite o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f'Depósito de R$ {valor:.2f}\n'
            print(f'Depósito de R$ {valor:.2f} realizado com sucesso.')
        else:
            print('Operação falhou! O valor informado é inválido.')

    elif opcao == '2':
        if numero_saques < LIMITE_SAQUE:
            valor = float(input("Digite o valor do saque: "))
            if valor <= limite and valor <= saldo:
                saldo -= valor
                extrato += f'Saque de R$ {valor:.2f}\n'
                numero_saques += 1
                print(f'Saque de R$ {valor:.2f} realizado com sucesso.')
            elif valor > saldo:
                print('Saldo insuficiente para realizar o saque.')
            else:
                print(f'Valor de saque excede o limite de R$ {limite:.2f}.')
        else:
            print('Limite de saques diários atingido.')

    elif opcao == '3':
        print('--- Extrato ---')
        print(extrato)
        print(f'Saldo atual: R$ {saldo:.2f}')

    elif opcao == '0':
        print('Saindo do programa...')
        break

    else:
        print('Opção inválida. Por favor, escolha uma opção válida.')
