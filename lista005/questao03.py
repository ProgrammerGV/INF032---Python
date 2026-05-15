estado = input("Sigla do estado: ").upper()
naturalidade = {"RJ": "Carioca", "SP": "Paulista", "MG": "Mineiro"}
print(naturalidade.get(estado, "Outros estados"))