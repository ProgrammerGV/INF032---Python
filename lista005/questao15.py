salario = float(input("Salário bruto: R$"))
prestacao = float(input("Valor da prestação: R$"))
print("Empréstimo CONCEDIDO" if prestacao <= salario * 0.30 else "Empréstimo NÃO concedido")