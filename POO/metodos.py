class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar(cls, ano, mes, dia, nome):
        idade = 2022 - ano
        return cls(nome, idade)

    @staticmethod
    def maior(idade):
        return idade >= 18


p = Pessoa.criar(2005, 6, 12, "Kassio")

print(p.nome, p.idade)
print(Pessoa.maior(p.idade))