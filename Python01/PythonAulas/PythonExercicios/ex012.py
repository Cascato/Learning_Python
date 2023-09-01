import math
raio = float(input('Digite o angulo que voce deseja: '))

r = math.radians(raio)
s = math.sin(r)
c = math.cos(r)
t = math.tan(r)

print(f'O angulo de {raio} tem o SENO de {s:.2f}')
print(f'O angule de {raio} tem o COSSENO de {c:.2f}')
print(f'O angulo de {raio} tem o TANGENTE de {t:.2f}')