'''
QUESTÃO
 Paulinho tem em suas mãos um novo problema. Agora a sua professora lhe pediu que
 construísse um programa para verificar, à partir de dois valores muito grandes
 A e B, se B corresponde aos últimos dígitos de A.
 ENTRADA
 A entrada consiste de vários casos de teste. A primeira linha de entrada contém um
 inteiro N que indica a quantidade de casos de teste. Cada caso de teste consiste de
 dois valores A e B maiores que zero, cada um deles podendo ter até 1000 dígitos.

 SAÍDA
 Para cada caso de entrada imprima uma mensagem indicando se o segundo valor encaixa
 no primeiro valor, confome exemplo abaixo.

IMPORTANTE: As funções "input" e "print" são acessíveis nativamente em Python, onde:
 - "input": função que permite a leitura de uma entrada do usuário. Lembre-se que, em alguns
   casos, é necessário converter/tratar os dados de entrada;
 - "print": função que imprime um texto enviado em seu parâmetro, a qual é essencial para a
   impressão dos dados de saída.

TODO  Verifique, para cada entrada A e B, se os dois valores são compatíveis e imprima se
"encaixa" ou "não encaixa" para cada uma das relações N vezes.

https://github.com/eduardo-mior/URI-Online-Judge-Solutions/blob/master/Strings/URI%201241.java

https://www.life2coding.com/uri-online-judge-solution-1241-fit-or-dont-fit-ii-intermediate-problem/

'''
'''
N = int(input())


while(N > 0):
    # A = int(input())
    # B = int(input())
    A = '123456789'
    B = '5656'

    if B in A:
        print("encaixa")
    else:
        print("não encaixa")
    N -= 1


'''
# https://github.com/pietrosonza/python_dio/blob/main/exercise3_mod1

n = int(input())


while n > 0:


    values = input().split()


    aux = ''
    for digit in values[0][::-1]:
        aux += digit
        if aux == values[1][::-1]:
            print('encaixa')
            break
    else:
        print('nao encaixa')


    aux = ''


    n -= 1
