nome1 = input("Digite o nome do primeiro jogador: ")
nome2 = input("Digite o nome do segundo jogador: ")

valor1 = int(input(f"Digite o valor que {nome1} colocou: "))
valor2 = int(input(f"Digite o valor que {nome2} colocou: "))

escolha1 = input(f"{nome1}, você escolhe 'ímpar' ou 'par'? ").strip().lower()

soma = valor1 + valor2

if (soma % 2 == 0 and escolha1 == "par") or (soma % 2 != 0 and escolha1 == "ímpar"):
    print(f"{nome1} ganhou a brincadeira!")
else:
    print(f"{nome2} ganhou a brincadeira!")
