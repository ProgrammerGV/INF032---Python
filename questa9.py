import math

base = 10
altura = 5

area = base * altura
perimetro = (2 * base) + (2 * altura)
diagonal = math.sqrt((base ** 2) + (altura ** 2))

print(f'perímetro: {perimetro} / área: {area} / diagonal: {diagonal:.2f}')