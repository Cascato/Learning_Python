from time import sleep
from random import randint

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
n = int(input('Em que número eu pensei? '))
ale = randint(0, 5)
print('PROCESSANDO...')
sleep(2)
if n == ale:
    print('PARABÉS! Você conseguiu me vencer!')
else:
    print(f'Otario! Perdeu pra maquina!! Pensei no {ale}!!');
