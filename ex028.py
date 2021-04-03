print("\033[;1m"'-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-')
print("\033[1;34m"'Vou pensar em um número entre 0 e 5. Tente adivinhar. . .')
print("\033[;1m"'-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-')
num = int(input('Em que número eu estou pensando? '))
from random import choice # faz a escolha aleatoria
from time import sleep # pra por tempo nas falas do console
lista = [0, 1, 2, 3, 4, 5]
n1 = choice(lista)
print("\033[1;34m"'PROCESSANDO. . .')
sleep(0.5)
print("\033[1;34m"'PROCESSANDO. . .')
sleep(0.5)
print("\033[1;34m"'PROCESSANDO. . .')
sleep(0.5)
if num == n1:
    print("\033[0;32m"'ACERTOU!' "\033[;1m"' Caramba, você é bom!')
else:
    print("\033[1;31m"'ERROU!'"\033[;1m"' Eu pensei no número {}'.format(n1))
