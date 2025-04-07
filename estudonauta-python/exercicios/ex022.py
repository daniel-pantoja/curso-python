# Crie um programa que leia o nome completo.
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo tem (sem considerar espaços).

nome = str(input('Digite seu nome completo: ')).strip() # strip --> Remove espaços antes e depois.

print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome) - nome.count(' ')} letras') # len(nome) - nome.count(' ') --> Vai contar quantas letras tem menos os espaços.

# print(f'Seu primeiro nome tem {nome.find(' ')} letras')

separa_nome = nome.split()

print(f'Seu primeiro nome é {separa_nome[0]} e ele tem {len(separa_nome[0])} letras') 
