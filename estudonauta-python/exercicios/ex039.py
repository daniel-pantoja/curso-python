# Alistamento Militar
# Faça um programa que leia o ano de nascimento de um jovem e informe
# De acordo com sua idade se ele ainda vai se alistar ao serviço militar
# Se é a hora de se alistar ou se já passou do tempo do alistamento
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento

print(f'Quem nasceu em {nascimento} tem {idade} anos em {atual}')

if idade == 18:
  print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
  saldo = 18 - idade
  print(f'Ainda faltam {saldo} anos para o alistamento')
  ano = atual + saldo
  print(f'Seu alistamento será em {ano}')
else:
  saldo = idade - 18
  print(f'Você já deveria ter se alistando há {saldo}')
  ano = atual - saldo
  print(f'Seu alistamento foi em {ano}')