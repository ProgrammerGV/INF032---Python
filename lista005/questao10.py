municipio = input("Nome do município: ")
eleitores = int(input("Eleitores aptos: "))
votos_1 = int(input("Votos do 1º colocado: "))
 
if eleitores > 20000 and votos_1 / eleitores <= 0.50:
    print(f"{municipio} TERÁ segundo turno")
else:
    print(f"{municipio} NÃO terá segundo turno")