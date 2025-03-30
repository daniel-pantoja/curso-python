# Crie uma função que receba um inteiro como argumento e retorne "Even" para números pares ou "Odd" impares.

# Lógica:
# Se a divisão por 2 tiver resto 0 - retorno "Even" par
# Se não, retorno "Odd" impar


def even_or_add(number):
    if number % 2 == 0:
        return "Even"
    
    return "Odd"