nome = str(input('Qual é seu nome? '))
if nome == 'Daniel':
  print(f'Nome lindo! {nome}')
else:
  print(f'Seu nome é tão normal, {nome}!')

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2 
print(f'A sua média foi {m:.2f}')

# Condição simples
if m >= 6.0:
  print('Sua média foi boa! PARABÉNS!') 
else:
  print('Sua média foi ruim! ESTUDE MAIS!')
# Condição simplificada 
print('Parabéns!' if m >=6 else 'Estude mais!')
