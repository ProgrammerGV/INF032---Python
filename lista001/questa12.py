import math

comprimento = 15
largura = 10
altura = 13
volume_pote = comprimento * largura * altura

raio = 1.2
volume_bolinha = (4/3) * math.pi * (raio ** 3)

fator = 0.74
volume_util = volume_pote * fator

quantidade_bolinhas = int(volume_util / volume_bolinha)

print(f'Cabem {quantidade_bolinhas} bolinhas de queijo no pote!')