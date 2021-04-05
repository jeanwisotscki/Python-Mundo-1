# Colhendo os dados:
nome = input('Digite o nome do colaborador: ').strip().title().split()
sal = float(input(f'Digite o salário atual de {nome[0]}: R$'))

# Variavéis:
aum1 = (sal*15)/100
aum2 = (sal*10)/100

# Solução:
if sal > 1250:
    nsal = sal + aum2
else:
    nsal = sal + aum1

# Exibir o resultado:
print(f'O novo salário de {nome[0]} vai ser R${nsal:.2f}')
