estoque = {"teclado": 12, "mouse": 5, "monitor": 2, "headset": 8}
pedidos = [{"produto": "mouse", "qtd": 3}, {"produto": "monitor", "qtd": 4},
           {"produto": "teclado", "qtd": 5}, {"produto": "webcam", "qtd": 1}]
 
pendentes = []
for pedido in pedidos:
    p, q = pedido["produto"], pedido["qtd"]
    if p in estoque and estoque[p] >= q:
        estoque[p] -= q
    else:
        pendentes.append(pedido)
 
print("Estoque atualizado:", estoque)
print("Pedidos pendentes:", pendentes)