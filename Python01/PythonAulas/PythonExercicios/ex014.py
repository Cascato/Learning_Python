import random
p = input('Primeiro aluno: ')
s = input('Segundo aluno: ')
t = input('Quarto aluno: ')
q = input('Quinto aluno: ')

lista = [p, s, t, q]
random.shuffle(lista)

print(f'A ordem de apresentação sera: {lista}')

