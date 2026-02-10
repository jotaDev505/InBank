class Cliente:
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, dataNascimento):
        self._cpf = cpf
        self._nome = nome
        self._dataNascimento = dataNascimento


class Conta:
    def __init__(self, saldo, numero, agencia, cliente, historico):
        self._saldo = saldo
        self._numero = numero
        self._agencia = agencia
        self._cliente = cliente
        self._historico = Historico()

    def saldo(self, saldo):
        return saldo

    def nova_conta(self, cliente, numero):
        self.cliente = cliente
        self.numero
        return Conta()

    def sacar(self, valor):
        saldo = self.saldo
        exedeu_valor = valor > saldo
        print('SAQUE SELECIONADO (Limite de R$500,00 por saque e 3 saques por dia!)')
        while True:
            if exedeu_valor:
                print('Quantia não aceita! Por favor digite uma quantia válida: ')
                return False
            else:
                saldo =- valor
                return True

    def depositar(self, valor):
        saldo = self.saldo
        if valor > 0:
            saldo += valor
            return True
        else:
            return False

