nome = str(input('Digite seu nome:')).strip()

print('Seu nome em maiuscula é', nome.upper())
print('Seu nome em minuscula é', nome.lower())


print('Seu nome tem ao todo', len(nome) - nome.count(' '), 'letras')

first = nome.split()
print(f'Seu primeiro nome é', nome.split()[0], 'e ele tem', len(first[0]), 'letras')
