frase = input('Digite a sua frase: ').strip().lower()
print('A sua frase possui {} letras A.'.format(frase.count('a')))
print('A primeira letra A da sua frase está na casa: {}'.format(frase.find('a')+1))
print('A ultima letra A da sua frase aparece na casa: {}'.format(frase.rfind('a')+1))
