pessoas = 5

total_cerveja = 75 * 2.20
total_macarrao = 2 * 8.73
total_molho = 1 * 3.45

total_cebola = (420 / 1000) * 5.40

total_alho = (250/1000) * 30

total_paes = (450/1000) * 25

total_compra = total_cerveja + total_macarrao + total_molho + total_cebola + total_alho + total_paes

valor_por_pessoa = total_compra / pessoas

print(f'O valor total foi R$ {total_compra:.2f}')

print(f'Cada um deve pagar R$ {valor_por_pessoa:.2f}')