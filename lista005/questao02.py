nome = input("Nome: ")
idade = int(input("Idade: "))
sexo = input("Sexo (M/F): ").upper()
print("ACEITA" if sexo == "F" and idade < 25 else "NAO ACEITA")
 