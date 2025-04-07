frase = '  Aprendendo Python'
print(frase)
print(frase[3])
print(frase[:10])
print(frase[5:])
print(frase[4:13])
print(frase[1:16:2])

print(frase.count('o')) # count --> Conta quantas vezes aparece 'o'.
print(frase.upper().count('O')) # upper --> Converter o 'o' para maiusculo.
print(len(frase)) #! len --> Mostra o tamanho da frase
print(len(frase.strip())) # strip --> Remove espaço indesejável.
print(frase.replace('Python', 'Programar'))
print(frase.strip().replace('Python', 'Programar'))

print(frase)
frase = frase.replace('Python', 'Programação')
print(frase) 
print(frase.strip())

print('Programação' in frase) # in --> Verifica se tem a palavra 'Programação' na frase. 
print(frase.find('Programação')) # Verifica em qual a posição está a frase 'Programação'. Mostrou a posição 13 por causa dos espaços
print(frase.split())
