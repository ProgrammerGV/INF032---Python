lista = [3, 8, 15, 4, 7, 2, 11, 6]
resultado = {"pares": [x for x in lista if x % 2 == 0],
             "impares": [x for x in lista if x % 2 != 0]}
 
print(resultado)
print("mais pares" if len(resultado["pares"]) > len(resultado["impares"]) else "mais ímpares")
if resultado["pares"]:
    print("Maior par:", max(resultado["pares"]))
if resultado["impares"]:
    print("Maior ímpar:", max(resultado["impares"]))