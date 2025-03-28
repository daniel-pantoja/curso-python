# São estruturas que permitem ao nosso programa tomar decisões com base em determinadas condições

# Exemplo:

# Você está em uma cafeteria e está com pouca grana
# SE você tiver 10 reais compra um café mais caro
# SE NÃO, pede p café simples.

# if confição: 
 # Executado se a condição for verdadeiro
# elif outra_condição
 # Executa se a primeiro for falsa, mas essa for verdadeira
# else:
 # Executa se nenhuma das condições anteriores for verdadeiro

idadeEv = int(input("Digite sua idade: "))
if idadeEv >= 18:
  print("Você pode entrar para o evento")
else: 
  print("Você é menor de idade, não pode entrar no evento")

idadeF = int(input("Digite sua idade: "))
if idadeF >= 18:
  print("Você pode assistir o filme +18")
else: 
  print("Desculpe, você ainda não tem idade suficiente para assistir o filme")  

nota = float(input("Digite sua nota: "))
if nota >= 7:
  print("Parabéns! Você passou de ano!")
elif nota >= 5:
  print("Você está de recuperação. Estude mais")
else: 
  print("Infelizmente, você foi reprovado.")

cafe = float(input("Digite o dinheiro que você tem para tomar café: "))
if cafe >= 12:
  print("Você pode adquirir um caputino, com rosquinha e um pão")
elif cafe >= 50:
  print("Cara você pode comprar até uma picanha")
else: 
  print("Você só pode comprar um café simples")
