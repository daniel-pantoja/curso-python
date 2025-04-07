# Faça um programa que leia o nome completo de uma pessoa.
# Mostra em seguida o primeiro e o último nome separadamente.

nome = str(input('Qual o seu nome completo? ')).strip()
nome_s = nome.split()

print(f'Muito prazer em te conhecer! {nome}')
print(f'Seu primeiro nome é {nome_s[0]}')
print(f'Seu último nome é {nome_s[len(nome_s)-1]}')
