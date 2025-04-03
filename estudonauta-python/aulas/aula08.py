# Utilizando Módulos

# Primeira Importação
# Exemplo 1
import math 
numero = int(input('Digite um número para ver a raiz: '))
raiz = math.sqrt(numero)
print(f'A raiz de {numero} é igual a {raiz:.2f}')

# Segunda Importação
# Exemplo 2 
from math import sqrt, floor
num = int(input('Digite um número: '))
raiz = sqrt(num)
print(f'A raiz de {num} é igual a {floor(raiz):.2f}')

