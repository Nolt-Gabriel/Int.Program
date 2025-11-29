aluno = {}

aluno["nome"] = input("Nome do aluno: ")
aluno["media"] = float(input("Média do aluno: "))

if aluno["media"] >= 7:
    aluno["situacao"] = "Aprovado"
elif aluno["media"] >= 5:
    aluno["situacao"] = "Recuperação"
else:
    aluno["situacao"] = "Reprovado"

print("-=" * 20)
for chave, valor in aluno.items():
    print(f"{chave.capitalize()}: {valor}")
