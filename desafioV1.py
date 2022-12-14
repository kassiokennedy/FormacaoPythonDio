from abc import ABC, abstractclassmethod, abstractclassproperty
from datetime import datetime

'''
Desafio do sistema bancario com POO

'''


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizarTransacao(self, conta, transacao):
        transacao.registrar(conta)

    def addConta(self,conta):
        self.contas.append(conta)


class PessoaFisica:
    def __init__(self, nome, nascimento, cpf, endereco):
        super().__init__(endereco) # chama o contrutor da classe pai
        self.nome = nome
        self.nascimento = nascimento
        self.cpf = cpf


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def novaConta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

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

    def sacar(self, valor):
        saldo = self.saldo  # recupera e verifica o saldo
        maiorquesaldo = valor > saldo  # verifica se o valor a sacar é maior que o saldo

        if maiorquesaldo:  # mensagem de erro
            print("Saldo insuficiente.")
        elif valor > 0:
            self._saldo -= valor
            print("Saque realizado.")
            return True
        else:
            print("Operação não realizada!")
        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("Deposito realizado.")
        else:
            print("Operação não realizada!")
            return False
        return True


class ContaCorrente:
    def __init__(self, numero, cliente, limite = 500, limitesaque=3):
        super().__init__(numero,cliente)  # construtor da classe
        self.limite = limite
        self.limitesaque = limitesaque

    def sacar(self, valor):
        numero




class Historico:
    pass


class Transacao(ABC):
    pass


class Saque(Transacao):
    pass


class Deposito(Transacao):
    pass

