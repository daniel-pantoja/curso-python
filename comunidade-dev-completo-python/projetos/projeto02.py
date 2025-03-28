# Simulando um Caixa Eletrônico

# O usuário tem um saldo inicial de R$ 500 e pode sacar dinheiro até o saldo zerar ou encerrar.

saldo = 500
saque = 0
print(f"Seu saldo R${saldo}")

while saldo > 0:
  saque = float(input("Informe o valor do saque: "))
  
  if saque > saldo:
    print("Saldo insuficiente! Saque não efetuado.")
    print(f"Saldo R$ {saldo:.2f}")
  else: 
    saldo -= saque
    print(f"Saque efetuado! Novo saldo R${saldo:.2f}")