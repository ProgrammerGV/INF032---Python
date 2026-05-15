precos = {"arroz": 22.0, "feijao": 8.5, "carne": 39.9, "leite": 5.5, "suco": 12.0}
compras = ["arroz", "carne", "suco", "pao", "leite", "biscoito"]
 
total = 0
indisponiveis = []
for item in compras:
    if item in precos:
        total += precos[item]
    else:
        indisponiveis.append(item)
 
if total > 500:
    desconto, pct = total * 0.10, "10%"
elif total >= 300:
    desconto, pct = total * 0.05, "5%"
else:
    desconto, pct = 0, "0%"
 
print(f"Total bruto: R${total:.2f} | Desconto: {pct} (R${desconto:.2f}) | Total final: R${total - desconto:.2f}")
print("Indisponíveis:", indisponiveis)