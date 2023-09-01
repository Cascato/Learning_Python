from random import choice
p = input('Primeiro aluno: ')
s = input('Segundo aluno: ')
t = input('Quarto aluno: ')
q = input('Quinto aluno: ')
lista = [p, s, t, q]
randola = choice(lista)
print(f'O aluno sera: {randola} ')
