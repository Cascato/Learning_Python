from math import hypot
O = float(input('Comprimento do cateto oposto: '))
A = float(input('Comprimento do cateto adjacente: '))
hi = hypot(O, A)
print(f'a hipotenusa vai medir: {hi:.2f}')
