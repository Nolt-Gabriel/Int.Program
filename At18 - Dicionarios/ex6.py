time = []

while True:
    jogador = {}
    gols = []

    jogador["nome"] = input("Nome do jogador: ")
    partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

    for p in range(partidas):
        gol = int(input(f"Gols na partida {p+1}: "))
        gols.append(gol)

    jogador["gols"] = gols[:]
    jogador["total"] = sum(gols)

    time.append(jogador)

    op = input("Quer cadastrar outro jogador? [S/N] ").strip().upper()
    if op == "N":
        break

print("-=" * 30)
print(f'{"cod":<4}{"nome":<10}{"gols":<15}{"total":>5}')
for i, j in enumerate(time):
    print(f'{i:<4}{j["nome"]:<10}{str(j["gols"]):<15}{j["total"]:>5}')


while True:
    idx = int(input("\nMostrar dados de qual jogador? (999 interrompe) "))
    if idx == 999:
        break
    if 0 <= idx < len(time):
        print(f"-- LEVANTAMENTO DO JOGADOR {time[idx]['nome']}:")
        for p, g in enumerate(time[idx]["gols"]):
            print(f"   No jogo {p+1} fez {g} gols.")
    else:
        print("Código inválido!")
