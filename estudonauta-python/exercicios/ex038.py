# Escreva um programa que leia dois números inteiros e compare-os.
# Mostre na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não Existe valor maior, os dois são iguais.

primeiro_numero = int(input("Primeiro número: "))
segundo_numero = int(input("Segundo número:"))

if primeiro_numero > segundo_numero:
    print("O PRIMEIRO  valor é maior")
elif segundo_numero > primeiro_numero:
    print("O SEGUNDO valor é maior")
else:
    print("Os dois valores são iguais")