# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada digitos separados.
# Ex: Digite um número: 1823
# Unidade:3 Dezena:2 Centena:8 Milhar:1

numero = int(input('Informe um número: '))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

print(f'Analisando o número {numero}')
print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')
