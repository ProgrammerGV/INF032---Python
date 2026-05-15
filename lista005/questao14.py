aluno = {"nome": "Ana", "notas": [6.5, 1.8, 8.0]}
media = sum(aluno["notas"]) / len(aluno["notas"])
aluno["status"] = "aprovado" if media >= 7 else ("reprovado" if media <= 3 else "prova final")
aluno["atencao"] = any(n < 2 for n in aluno["notas"])
print(aluno)