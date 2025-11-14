n = int(input("Digite a quantidade de notas: "))
notas = []

for i in range(n):
    nota = float(input(f"Digite a nota {i+1}: "))
    notas.append(nota)
    
media = sum(notas) / n

acima = []
abaixo = []

for nota in notas:
    if nota > media:
        acima.append(nota)
    elif nota < media:
        abaixo.append(nota)

print(f"Média da turma: {media:.2f}")
print(f"{len(acima)} nota(s) acima da média: {acima}")
print(f"{len(abaixo)} nota(s) abaixo da média: {abaixo}")
