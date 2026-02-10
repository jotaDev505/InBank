from time import sleep

def menuInicial():
    print('''
            Selecione o número da operação desejada:
            [1] - LOGIN
            [2] - CADASTRAR USUÁRIO
            ''')
    print()
    return int(input('Digite o número: '))


def login(userList):
    print('LOGIN SELECIONADO')
    sleep(1)
    print('-'*30)
    nome = str(input('Nome: '))
    cpf = input('CPF: ')
    for usuario in userList:
        if usuario['nome'] == nome and usuario['cpf'] == cpf:
            print('Logado com sucesso!')
    return usuario


def registerUser(userList):
    print('Registrar Usuário')
    sleep(1)
    print('-'*30)
    user = {
        'nome': str(input('Nome: ')),
        'dataNascimento': str(input('Data de Nascimento: ')),
        'cpf': int(input('Diogite seu CPF: ')),
        'endereco': {
            'logradouro': str(input('Digite o logradouro: ')),
            'numero': int(input('Digite o Número: ')),
            'bairro': str(input('Digite o Bairro: ')),
            'cidade': str(input('Digite a Cidade: ')),
            'estado': str(input('Sigla do Estado: ').upper()),
        },
        'contas': {'conta': 0,
                   'banco': '0001',
                   'proprietario': 'cpf',
                   'saldo': 0,
                   'extrato': [],
                   'qtdOut': 0
                   }
        }
    for usuario in userList:
        if usuario['cpf'] == user['cpf']:
            print('ERRO!!')
            print(f"Usuário com CPF({user['cpf']}) já existe no sistema!")
            main()
        userList.append(user)
        print('Registrado com sucesso!')
        print(userList)


def criarConta(usuario):
    novaConta = {'conta': len(usuario['contas'])+ 1,
                 'banco': '0001',
                 'proprietario': usuario['cpf'],
                 'saldo': 0,
                 'extrato': [],
                 'qtdOut': 0
                 }
    usuario['contas'].append(novaConta)
    print('Criando Conta.', sleep(1), '.', sleep(1), '.')
    print('CONTA CRIADA COM SUCESSO!')
    print(novaConta)


def actions():
    print('''
        Selecione o número da operação desejada:
        [1] - DEPÓSITO
        [2] - SAQUE
        [3] - EXTRATO
        [4] - CRIAR CONTA
        [5] - Sair
        ''')
    choice = int(input('Digite o número: '))
    print()
    if choice not in (1, 2, 3, 4,5):
        print('Erro! Pr favor digite os números 1, 2, 3, 4 ou 5!.')
        actions()
    else:
        return choice


def depositar(account, valor, extractList, /):
    account += valor
    extractList.append(f'{valor:.2f}')
    print('R$', account)
    return account, extractList


def saque(saldo, valor, extrato, limite, qtdSaques, limiteSaque):
    cashOut = 0
    print('SAQUE SELECIONADO (Limite de R$500,00 por saque e 3 saques por dia!)')
    while True:
        if qtdSaques == 3:
            print('LIMITE DE SAQUE DIÁRIO ALCANÇADO')
            break
        if valor >= 500 or valor > saldo:
            print('Quantia não aceita! Por favor digite uma quantia válida: ')
            break
        else:
            saldo -= valor
            qtdSaques += 1
            extrato.append(f'-{valor:.2f}')
            break
    return saldo, extrato, qtdSaques

def extract(saldo, /, *, extrato):
    print('---EXTRATO---')
    for c, i in enumerate(extrato):
        print(f'R$ {i}')
    print('\n')
    print(f'Total em conta: R${saldo:.2f}')


def main():
    limiteSaque = 3
    limite = 500.00
    inicio = menuInicial()
    if inicio == 1:
       usuario = login(userList)
       print(usuario)
    else:
        registerUser(userList)
    inicio = 0
    while True:
        opcao = actions()
        if opcao == 1:
            print('DEPÓSITO SELECIONADO')
            sleep(0.5)
            usuario['saldo'], usuario['extrato'] = depositar(usuario['saldo'], float(input('Qual valor deseja depositar? ')) ,usuario['extrato'])
            print(usuario)
        elif opcao == 2:
            print('SAQUE SELECIONADO')
            sleep(0.5)
            usuario['saldo'], usuario['extrato'], usuario['qtdOut'] = saque(saldo=usuario['saldo'], valor=float(input('Digite o valor do saque: ')), extrato=usuario['extrato'], limite=limite, qtdSaques=usuario['qtdOut'], limiteSaque=limiteSaque)
            print(usuario)
        elif opcao == 3:
            print('EXTRATO SELECIONADO')
            sleep(0.5)
            extract(usuario['saldo'], extrato=usuario['extrato'])
        elif opcao == 4:
            print('Criação de Conta foi Selecionado')
            sleep(0.5)
            criarConta(usuario)
        elif opcao == 5:
            print('SAINDO DA CONTA')
            sleep(0.5)
            main()


userList = [{
        'nome': 'joao',
        'dataNascimento': '09-04-99',
        'cpf': 5,
        'endereco': {
            'logradouro': 'Joao Alves',
            'numero': 100,
            'bairro': 'Teste',
            'cidade': 'São Paulo',
            'estado': 'SP',
        },
        'contas': [],
    }]

main()