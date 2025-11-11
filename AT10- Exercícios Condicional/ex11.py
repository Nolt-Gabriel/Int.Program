time1 = input("Digite o nome do primeiro time: ")
gols1 = int(input(f"Digite a quantidade de gols do {time1}: "))
time2 = input("Digite o nome do segundo time: ")
gols2 = int(input(f"Digite a quantidade de gols do {time2}: "))

if gols1 > gols2:
    print(f"O time vencedor é: {time1}")
elif gols2 > gols1:
    print(f"O time vencedor é: {time2}")
else:
    print("A partida terminou empatada.")
