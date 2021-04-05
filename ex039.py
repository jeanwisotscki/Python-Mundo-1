# Importando bibliotecas:
from datetime import date

# Colhendo dados e variavéis:
atual = date.today().year
print('''Digite a opção que corresponda ao seu sexo
[ M ] para sexo MASCULINO
[ F ] para sexo FEMININO''')
sexo = input('Digite aqui a sua resposta: ').upper()

# Solução:
while sexo not in 'MF':
    sexo = input('Por favor, digite uma opção válida: ').upper()

if sexo == 'M':
    nasc = int(input('Qual o seu ano de nascimento? '))

    while nasc > atual:
        print('Opção inválida!')
        nasc = int(input('Qual o seu ano de nascimento? '))
    idade = atual - nasc
    print('Quem nasceu em {} já tem ou vai fazer {} anos em {}.'.format(nasc, idade, atual))

    if idade == 18:
        print('Você tem que se alistar imediatamente!')

    elif idade < 18:
        saldo = 18 - idade
        print('Ainda faltam {} anos para o alistamento.'.format(saldo))
        ano = atual + saldo
        print('Seu alistamento será em {}'.format(ano))

    else:
        saldo = idade - 18
        print('Você já deveria ter se alistado há {} anos.'.format(saldo))
        ano = atual - saldo
        print('Seu alistamento foi em {}'.format(ano))
else:
    print('O alistamento militar é obrigatório somente ao sexo MASCULINO! \n\033[:32mVocê está DISPENSADA.''\033[m')
