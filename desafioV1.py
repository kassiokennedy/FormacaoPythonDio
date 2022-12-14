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
        super().__init__(endereco)
        self.nome = nome


class Conta:
    pass


class CC:
    pass


class Historico:
    pass


class Transacao(ABC):
    pass


class Saque(Transacao):
    pass


class Deposito(Transacao):
    pass

