deposito = 500.00
juros = 0.01

for _ in range(3):
    deposito += deposito * juros

print(f"Saldo após 3 meses: R${deposito:.2f}")