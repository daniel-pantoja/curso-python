# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço. 
# Com 5% de desconto.

preco = float(input('Qual é o preço do produto? R$'))
n_preco = preco - (preco * 5 / 100)

print(f'O produto que custava R${preco:.2f}, na promoção com desconto de 5% vai custar R${n_preco:.2f}')