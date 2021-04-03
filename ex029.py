print('===============  D E T R A N - S C  ====================')
vel = int(input('Digite a velocidade que o veiculo passou: '))
ex = vel - 80
multa = ex * 7
if vel <= 80:
    print('O veiculo não excedeu o limite de velocidade da via.\nPortanto, não será multado.')
else:
    print('Veiculo excedeu o limite de velocidade da via em {}km/h. \nPortanto, será multado em R${:.2f}'.format(ex, multa))
print('=============== Dirija com cuidado! ====================')
