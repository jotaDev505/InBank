# A v1 do projetto deve possuir apenas um usuário.
# Somente possivel fazer 3 saques por dia com o limite de R$500,00
# Possível fazer saquem, depósito extrato.
# Modular o projeto em funções.

account = 0
extractList = []
qtdOut = 0
while True:
    print('''
    Selecione o número da operação desejada:
    [1] - DEPÓSITO
    [2] - SAQUE
    [3] - EXTRATO
    ''')
    choice = int(input('Digite o número: '))
    print()

    if choice == 1:
        print('DEPÓSITO SELECIONADO')
        cashDeposit = float(input('Qual valor deseja depositar? '))
        account += cashDeposit
        extractList.append(f'{cashDeposit:.2f}')
        print(account)

    if choice == 2:
        cashOut = 0
        print('SAQUE SELECIONADO (Limite de R$500,00 por saque e 3 saques por dia!)')
        while True:
            if qtdOut == 3:
                print('LIMITE DE SAQUE DIÁRIO ALCANÇADO')
                break
            cashOut = float(input('Quanto deseja sacar? '))
            if cashOut >= 500 or cashOut > account:
                print('Quantia não aceita! Por favor digite uma quantia válida: ')
            else:
                account -= cashOut
                qtdOut += 1
                extractList.append(f'-{cashOut:.2f}')
                break

    if choice == 3:
        print('---EXTRATO---')
        for c, i in enumerate(extractList):
            print(f'R$ {i}')
        print(f'Total em conta: R${account:.2f}')

    if choice not in (1, 2, 3):
        print('Erro! Pr favor digite os números 1, 2 ou 3.')
