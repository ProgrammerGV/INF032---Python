custo = float(input("Valor de compra do produto: R$"))
lucro = 0.45 if custo < 20 else 0.30
print(f"Valor de venda: R${custo * (1 + lucro):.2f}")