cidades = ["Ouro Preto", "Santos", "Belo Horizonte", "São Paulo", "Mariana", "Campinas"]
mapa = {"Ouro Preto": "MG", "Santos": "SP", "Belo Horizonte": "MG",
        "São Paulo": "SP", "Mariana": "MG", "Campinas": "SP"}
 
sigla = input("Sigla do estado: ").upper()
resultado = sorted([c for c in cidades if mapa.get(c) == sigla])
print(resultado if resultado else "nenhuma cidade encontrada")