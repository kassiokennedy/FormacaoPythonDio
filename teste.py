'''
 QUESTÃO
 Devita é o príncipe dos Calsadins. Juntamente com Pana, eles vão atrás de
 Tataroko, o nome de nascimento de Kogu, para tentar dominar o mundo. Ele
 possui um rastreador que mede o nível de energia de qualquer ser vivo.
 Todos os seres com o nível menor ou igual a 8000, ele considera como se
 fosse um inseto. Quando passa deste valor, que foi o caso de Kogu, ele se
 espanta e grita “Mais de 8000”. Baseado nisso, utilize a mesma tecnologia
 e analise o nível de energia dos seres vivos.

 ENTRADA
 A entrada é composta por vários casos de teste. A primeira linha contém um
 número inteiro C relativo ao número de casos de teste. Em seguida, haverá C
 linhas, com um número inteiro N (100 <= N <= 100000) relativo ao nível de
 energia de um ser vivo.

 SAÍDA
 Para cada valor lido, imprima o texto correspondente.


C = int(input())
for i in range(C):
    N = int(input())
    if N <= 8000:
      print("Inseto!")
    else:
      print("Mais de 8000!")

'''
# ---------------------------------------------------------------------------------
'''
 QUESTÃO
 Um supermercado está fazendo uma promoção de venda de refrigerantes. Se um dia 
 você comprar refrigerantes e levar os cascos vazios no dia seguinte, ela troca 
 cada conjunto de K garrafas vazias  por uma garrafa cheia. Um cliente quer 
 aproveitar ao máximo essa oferta e por isso comprou várias garrafas no primeiro 
 dia da promoção. Agora ele quer saber quantas garrafas terá ao final do segundo 
 dia da promoção, se usá-la ao máximo.
 Faça um programa para calcular isso.
 ENTRADA
 A primeira linha de entrada contém inteiro T (1 <= T <= 10000) , que indica o 
 número de casos de teste. Em cada uma das T linhas a seguir vêm dois inteiros 
 N e K (1 <= K, N <= 10000),  respectivamente o número de refrigerantes comprados 
 e o número de garrafas vazias para ganhar uma cheia.
 
 SAÍDA
 Para cada caso de teste imprima o número de garrafas que o cliente terá no 
 segundo dia, se aproveitar ao máximo a oferta.
 https://urisolutions.blogspot.com/2021/02/uri-problem-2896-solution-enjoy-offer.html
 
'''
'''

T = int(input())

S = 0
while T > 0:
    N, K = map(int, input().split())

    if N >= K:
        S = S + N / K
        S = S + N % K
    else:
        S = N
    print(int(S))
    S = 0
    T -= 1
'''

# --------------------------------------------------------------------------------
'''

https://github.com/MayaraMachado/URI---Python-3/blob/master/animal%20-%201049.py
'''


''' 
IMPORTANTE: As funções "input" e "print" são acessíveis nativamente em Python, onde:  
 - "input": função que permite a leitura de uma entrada do usuário. Lembre-se que, em alguns 
   casos, é necessário converter/tratar os dados de entrada; 
 - "print": função que imprime um texto enviado em seu parâmetro, a qual é essencial para a 
   impressão dos dados de saída. 
   http://muitomaiscodigoss.blogspot.com/2018/09/uri-problema-1049-animal-em-python.html
'''
x = input()
y = input()
z = input()

if x == 'vertebrado' and y == 'ave' and z == 'carnivoro':
    a = 'aguia'

if x == 'vertebrado' and y == 'ave' and z == 'onivoro':
    a = 'pomba'

if x == 'vertebrado' and y == 'mamifero' and z == 'onivoro':
    a = 'homem'

if x == 'vertebrado' and y == 'mamifero' and z == 'herbivoro':
    a = 'vaca'

if x == 'invertebrado' and y == 'inseto' and z == 'hematofago':
    a = 'pulga'

if x == 'invertebrado' and y == 'inseto' and z == 'herbivoro':
    a = 'lagarta'

if x == 'invertebrado' and y == 'anelideo' and z == 'hematofago':
    a = 'sanguessuga'

if x == 'invertebrado' and y == 'anelideo' and z == 'onivoro':
    a = 'minhoca'

print(a)