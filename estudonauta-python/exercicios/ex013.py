salario_f = float(input('Qual é o salário do funário? R$'))
n_salario = salario_f + (salario_f * 15 / 100) 

print(f'Um funcionário que ganhava R${salario_f:.2f}, com 15% de aumento, passa a receber R${n_salario:.2f}')