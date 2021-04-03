nome = input('Digite seu nome completo: ').strip().title()
n1 = nome.split()
print('Seja bem vindo, {}.'.format(nome))
print('Seu primeiro nome é {}.'.format(n1[0]))
print('Seu último nome é {}.'.format(n1[-1]))

''' o valor entre os colchetes é a posição do item que 
    vc quer acessar na lista. Ex: lista[0], se refere ao
    primeiro item da lista, lista[1] ao segundo e assim 
    por diante. Se vc utilizar valores negativos
    dentro do colchetes, vc acessa valores a partir do 
    final da lista, em direção ao inicio, 
    ou seja: lista[-1] se refere ao último item da lista, 
    lista[-2] ao penúltimo, etc.. '''



