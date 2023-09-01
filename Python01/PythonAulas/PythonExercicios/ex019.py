n = str(input('Digite uma frase: ')).strip().lower()
print(f'A letra A aparece', n.count('a'), 'vezes na frase')
print('A primeira letra A apareceu na posição', n.find('a')+1)
print('A ultima letra A apareceu na posição', n.rfind('a')+1)
