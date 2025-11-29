pessoas = []
soma_idades = 0

while True:
    pessoa = {}
    pessoa["nome"] = input("Nome: ")
    pessoa["sexo"] = input("Sexo [M/F]: ").strip().upper()
    pessoa["idade"] = int(input("Idade: "))

    soma_idades += pessoa["idade"]
    pessoas.append(pessoa)

    op = input("Quer continuar? [S/N] ").strip().upper()
    if op == "N":
        break

media = soma_idades / len(pessoas)

print("-=" * 30)
print(f"A) Total de pessoas cadastradas: {len(pessoas)}")
print(f"B) Média de idade: {media:.1f} anos")

print("C) Lista de mulheres:")
for p in pessoas:
    if p["sexo"] == "F":
        print(f"   - {p['nome']}")

print("D) Pessoas com idade acima da média:")
for p in pessoas:
    if p["idade"] > media:
        print(f"   - {p['nome']} ({p['idade']} anos)")
