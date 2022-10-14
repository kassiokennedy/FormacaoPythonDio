'''
https://academiapme-my.sharepoint.com/:p:/g/personal/kawan_dio_me/Ef-dMEJYq9BPotZQso7LUCwBJd7gDqCC2SYlUYx0ayrGNQ?rtime=6BGAHCWu2kg

'''
# Variavel global
saldo = 1000
i = 0
extrato = ''
class Banco:

    def __init__(self):
        pass
    # --------------------------------------------------------
    def depositar(self):
        global saldo
        global extrato
        deposito = float(input("\nDeposite seu dinheiro: "))
        if deposito <= 0:
            print("\nNao é permitido deposito negativo ou valor zero.")
        else:
            saldo += deposito
        extrato += f'\nDepósito: {deposito:.2f} R$'
        return print(f'Seu saldo é de {saldo:.2f} R$\n')
    # -------------------------------------------------------
    def sacar(self):
        global saldo # chamada da variavel global
        global i
        global extrato
        if saldo > 0 and i <=4: # Verifica se ha saldo para a operacao
            saque = float(input(
                f'\nSeu saldo é de {saldo:.2f} R$\n'
                f'Informe o valor do saque: '))
            if saque <= 0 or saque > 500:
                return print("Operação inválida!.")
            else:
                saldo -= saque
            extrato += f'\nSaque: {saque:.2f} R$'
            i += 1
        else:
            if saldo <= 0:
                print("\nSaldo insuficiente.")
            else:
                print("\nSeulimite é de ate 3 saques diários.")

        return print(f'\nSeu saldo é de {saldo:.2f} R$\n')
    # -------------------------------------------------------
    def extrato(self):
        if not extrato:
            print(f'''
-------------------- Extrato --------------------------- 
            Não ha movimentações.
--------------------------------------------------------
                        ''')
        else:
            print(f'''
-------------------- Extrato --------------------------- 
{extrato}
\nSeu saldo é de {saldo:.2f} R$\n
--------------------------------------------------------
            ''')

#################################################################
#################################################################
#################################################################

print(__name__)
if __name__ == '__main__':
    # instanciando a classe Banco
    banco = Banco()

    while True:
        # Menu de opções
        operacao = int(input(
            f'''
-------------------- Menu ------------------------------ 
        1 - Saque
        2 - Depósito
        3 - Extrato
        4 - Sair 
--------------------------------------------------------
Escolha uma operação:'''))
        if operacao == 1:
            print(banco.sacar())
        elif operacao == 2:
            print(banco.depositar())
        elif operacao == 3:
            print(banco.extrato())
        elif operacao == 4:
            print("\nFechando o programa.")
            break
        i += 1