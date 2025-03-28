# Definida entre colchetes 
# Pode amazenar diferentes tipos de dados.

frutas = ["maçã", "banana", "laranja"]
numeros = [1, 2, 3, 4, 5]
misturada = ["Daniel", 2.12, 10, True]

# Acessando elementos da lista
print(frutas[-1]) # O -1 conta de trás para frente
print(frutas[0])
print(frutas[1])

print(frutas)
frutas[1] = "uva"
print(frutas)

# Adicionando elementos á lista
# append(): --> adiciona um item ao final
# insert(): --> adiciona item em posição específica

numeros = [1, 2, 3]
print(numeros)

numeros.append(4)
print(numeros)

numeros.insert(1, 10) # (posição, valor) 
print(numeros) # [1, 10, 2, 3, 4] (inseriu na posição 1 o valor 10)

# Removendo elementos da lista 

# remove(): remove um item pelo valor
# pop(): remove um item pelo índice ou o último item se nenhum índice for passado

frutas = ["maçã", "banana", "uva", "laranja"]
print(frutas)
frutas.remove("banana")
print(frutas)

frutas.pop(0)
print(frutas)

frutas.pop() # removeu o ultimo item
print(frutas)

# Tuplas
cores = ("Vemelho", "Azul", "Verde")
numeros = (1, 2, 3, 4, 5)

print(cores[0])
print(cores[-1])
print(numeros[0])
print(numeros[4])

# Convertenddo entre lista e tupla
tupla = (1, 2, 3)
lista = list(tupla)
lista.append(4)
tupla = tuple(lista)
print(tupla)

meses = ("Janeiro", "Fevereiro", "Março", "Abril")
print(meses)
print(meses[2])
