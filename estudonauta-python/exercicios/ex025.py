# Crie um programa que leia o nome de uma pessoa e diga se ela tem "PANTOJA" no nome.

nome = str(input('Qual é seu nome: ')).strip()
print(f'Seu nome tem Pantoja? {'PANTOJA' in nome.upper()}')
