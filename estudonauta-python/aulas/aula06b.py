# Inteiro 
idade = int(input('Qual a sua idade? '))
print('Sua idade é', idade)

# Ponto Flutuante 
altura = float(input('Qual a sua altura? '))
print('Sua altura é', altura,)

# String 
nome = input('Qual o seu nome? ')
print('Olá,', nome, '!')

# Booleano 
gprogramacao = input('Você gosta de programação? (sim/não) ').strip().lower() == 'sim'
print('Você gosta de programação:', gprogramacao)

n = input('Digite algo: ')
print(n.isnumeric())

na = input('Digite algo: ')
print(na.isalpha())

nb = input('Digite algo: ')
print(nb.isupper())