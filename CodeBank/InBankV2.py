from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

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

    @classmethod
    def saldo(self, saldo):
        return saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    @property
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)


    def sacar(self, valor):
        saldo = self.saldo
        exedeu_valor = valor > saldo

        print('SAQUE SELECIONADO (Limite de R$500,00 por saque e 3 saques por dia!)')

        if exedeu_valor:
            print('xxQuantia não aceita! Por favor digite uma quantia válida!xx')
        elif valor > 0:
            self._saldo =- valor
            print("==SAQUE REALIZADO COM SUCESSO==")
            return True
        else:
            print("xxFALHA NO SAQUExx")
        return False

    def depositar(self, valor):
        saldo = self.saldo
        if valor > 0:
            saldo += valor
            print("==DEPÓSITO REALIZADO COM SUCESSO==")
            return True
        return False

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao['tipo'] == Saque.__name__]
        )

        exedeu_limite = valor > self.limite
        exedeu_saques = numero_saques >= self._limite_saques

        if exedeu_limite:
            print("xxxOPERAÇÃO FALHOU! VALOR DO SAQUE EXEDEU O LIMITE!xxx")
        elif exedeu_saques:
            print("xxxO NUMERO DE SAQUE EXEDEU O LIMITE!xxx")
        else:
            return super().sacar(valor)
        return False

    def __str__(self):
        return f""""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
            """

class Historico:
    def __init__(self):
        self._transacoes = []

        @property
        def transacoes(self):
            return self._transacoes

        def adicionar_transacao(self, transacao):
            self._transacoes.append(
                {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                }
            )

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
