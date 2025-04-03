# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira. 

# Ex: Digite um número: 1.244
# O número 1.244 tem a parte inteira 6.


# Programa 1 
from math import trunc
numero = float(input('Digite um valor: '))
print(f'O valor digitado foi {numero} e a sua porção inteira é {trunc(numero)}')

# Programa 2
num = float(input('Digite um número: '))
print(f'O valor digitado foi {num} e a sua porção inteira é {int(num)}')