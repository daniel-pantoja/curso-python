# Simulando um Caixa Eletrônico

# O usuário tem um saldo inicial de R$ 500 e pode sacar dinheiro até o saldo zerar ou encerrar.

saldo = 500
saque = 0


while saldo > 0:
  saque = float(input("Informe o valor do saque: "))
  