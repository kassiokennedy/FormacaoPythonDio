class Banco:

    def __init__(self):
        pass

    def depositar(self):
        saldo = 0
        deposito = float(input("Deposite seu dinheiro: "))
        if deposito <= 0:
            print("Nao é permitido deposito negativo ou valor zero.")
        else:
            saldo += deposito
        return print(saldo)

    def sacar(self):

        saldo = 1000
        saque = float(input(
            f'Seu saldo é: {saldo}\n'
            f'Quanto deseja sacar? '))
        if saque <= 0:
            print("Nao é permitido sacar valor zero.")
            if saque > saldo:
                print("Saldo insuficiente.")
        else:
            saldo -= saque
        return print(saldo)

    def extrato(self):
        pass


print(__name__)
if __name__ == '__main__':
    # instanciando a classe Banco
    banco = Banco()

    # Menu de opções
    operacao = int(input(
    f'''
    Escolha uma opercação a realizar:
        1 - Saque
        2 - Depósito
        3 - Extrato
        4 - Sair
    '''
    ))
    # print(f'Você digitou {operacao}')

    if operacao == 1:
        print(banco.sacar())
    elif operacao == 2:
        print(banco.depositar())
