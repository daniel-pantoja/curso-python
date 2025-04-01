# Faça um programa que leia a largura e a altura de uma parede em metros.
# Calcule a sua área e a quantidade de tinta necessário para pintá-lo.
# Cada litro de tinta, pinta uma área de 2m².

largura = float(input('Largura da parede: '))
altura = float(input('Largura de parede: '))
areá = largura * altura

print(f'Sua parede tem a dimensão de {largura}x{altura} e a sua área é de {areá}m².')

l_tinta = areá / 2

print(f'Para pintar essa parede, você precisará de {l_tinta} litros de tinta.')