# Desenvolva um programa que leia as duas notas de um aluno.
# calcule e mostre a sua média.

nota1 = float(input("Primeira nota do aluno: "))
nota2 = float(input("Segunda nota do aluno: "))
média = (nota1 + nota2) / 2

print(f"A média entre {nota1:.1f} e {nota2:.1f} é igual a {média:.1f}")