# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5.
# Peça para o usuário tentar descobrir qual foi o número escolhido pelo computador
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
computador = randint(0,5) # Faz o computador "pensar"

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...') 
print('-=-' * 20)

jogador = int(input('Em que número eu pensei? ')) # Tentar adivinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computador: 
  print('Parabêns! Você conseguiu me vencer!')
else:
  print(f'Ganhei! Eu pensei no número {computador} e não no {jogador}')