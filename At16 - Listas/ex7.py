notas = []
k = 0

while k < 4:
    notas.append(float(input('Nota: ')))
    k = k + 1


soma = 0
k = 0
while k < 4:
    soma = soma + notas[k]
    k = k + 1

print(f'Notas: {notas}')
print(f'Média é {soma / 4:.1f}')
