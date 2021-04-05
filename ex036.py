# Colhendo os dados & Variavéis:
valor = float(input('Qual o valor do imóvel? R$'))
sal = float(input('Qual o seu salário? R$'))
anos = int(input('Em quantos anos gostaria de pagar? '))
meses = anos * 12
prest = valor / meses
porc = sal * 30 / 100

# Solução:
if prest > porc:
    print("\033[0;35m"'Infelizmente o valor das prestações desse financiamento irá ultrapassar '
          '\na margem de 30% do seu salário. Portanto, não será possivel prosseguir com este \n'
          'valor. Tente um valor menor.')
else:
    print("\033[0;32m"'Você está prestes a financiar esse imóvel! \nO financiamento será dividido em {} anos. '
          '\nNo total serão {} parcelas de R${:.2f} por mês.'.format(anos, meses, prest))
