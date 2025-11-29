alunos = []

while True:
    nome = input("Nome: ")
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    media = (n1 + n2) / 2

    alunos.append([nome, [n1, n2], media])

    op = input("Quer continuar? [S/N] ").strip().upper()
    if op == "N":
        break

print("-=" * 30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>7}')
print("-" * 25)
for i, a in enumerate(alunos):
    print(f'{i:<4}{a[0]:<10}{a[2]:>7.1f}')


while True:
    idx = int(input("\nMostrar notas de qual aluno? (999 interrompe) "))
    if idx == 999:
        break
    if 0 <= idx < len(alunos):
        print(f"Notas de {alunos[idx][0]} são {alunos[idx][1]}")
    else:
        print("Índice inválido!")
