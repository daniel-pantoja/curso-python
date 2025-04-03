# Faça um programa que leia um ângulo qualquer. 
# Mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math 
angulo = float(input('Digite o ângulo que você deseja: '))

seno = math.sin(math.radians(angulo))
print(f'O ângulo de {angulo} tem o SENO de {seno:.2f}')

cosseno = math.cos(math.radians(angulo))
print(f'O ângulo de {angulo} tem o COSSENO de {cosseno:.2f}')

tangete = math.tan(math.radians(angulo))
print(f'O ângulo de {angulo} tem a TANGENTE de {tangete:.2f}')