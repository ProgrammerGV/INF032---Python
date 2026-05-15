nome = input("Nome do aluno: ")
n1, n2 = float(input("Nota 1: ")), float(input("Nota 2: "))
media = (n1 + n2) / 2
if media >= 7:
    status = "Aprovado"
elif media < 3:
    status = "Reprovado"
else:
    status = "Prova Final"
print(f"Aluno: {nome} | N1: {n1} | N2: {n2} | Média: {media:.1f} | {status}")