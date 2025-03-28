# Repetir contagem automaticamente, sem precisar repetir o mesmo comando várias vezes

# Python tem dois tipos principais de laços:
# for --> Sabemos quantas vezes vamos repetir algo.
# while --> Quando queremos repetir algo até que uma condição se torne falsa.

for numero in range(1, 6): # range de (1, 6) -> 1 até 5
  print(numero)

for nome in range(1, 5):
  nome = "Daniel"
  print(nome)


frutas = ["Maçã", "Banana", "Morango", "Pêra"]

for item in frutas:
  print(f"Comer: {item}")


palavra = "DANIEL"

for letra in palavra:
  print(letra)
  
  
# While
contador = 5

while contador > 0:
  print(contador)
  contador -= 1 

print("Fogo!")


senha_correta = "10"
senha = ""

while senha != senha_correta:
  senha = input("Digite a senha: ")
  
print("Acesso permitido!")

s_correta = "10"
senha = ""
tentativas = 5

while senha != s_correta and tentativas > 0:
    senha = input("Digite a senha: ")
    tentativas -= 1
    if tentativas > 0 and senha != s_correta:
        print(f"Senha incorreta! Você ainda tem {tentativas} tentativas.")
        
if senha == s_correta:
    print("Acesso permitido!")
else:
    print("Acesso negado! Você excedeu o número de tentativas.")