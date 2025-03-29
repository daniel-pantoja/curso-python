# Blocos de código reutilizáveis que realizam uma tarefa específica.
# Criamos uma função e apenas a chamamos sempre que necessário.

def saudacao(nome):
    print(f"Olá, {nome} Bem-Vindo ao curso de Python.")
    
saudacao("Daniel")

# Retorno de valores
def somar(a, b):
    return a + b

resultado = somar(5, 4)
print(f"A soma é {resultado}")

def sub(a, b, c):
    return a - b - c

resultado = sub(10, 4, 2)
print(f"A subtração é {resultado}")

# Função com vários parametros
def calcular_media(n1, n2, n3):
    media = (n1, n2, n3) / 3
    return media 

resultado = calcular_media(8, 9, 7)
print(f"A média é {resultado:.2f}")