# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
# Considere US$1.00 = R$5.71

real = float(input('Quanto dinheiro você tem na carteira? '))
dolar = real / 5.71
print(f'Você informou que tem R${real:.2f}.')
print(f'Com esse valor, você pode comprar aproximadamente US${dolar:.2f}.')