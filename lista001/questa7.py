import math

graus = math.radians(80)

senograus = math.sin(graus)
cosgraus = math.cos(graus)
tangraus = math.tan(graus)
secgraus = 1 / cosgraus
cossecgraus = 1 / senograus
cotangraus = 1 / tangraus

print(f'Seno: {senograus:.4f}')
print(f'Cosseno: {cosgraus:.4f}')
print(f'Tangente: {tangraus:.4f}')
print(f'Secante: {secgraus:.4f}')
print(f'Cossecante: {cossecgraus:.4f}')
print(f'Cotangente: {cotangraus:.4f}')