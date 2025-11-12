from datetime import date

atual = date.today().year
maiores = 0
menores = 0

for i in range(7):
    nascimento = int(input(f"Digite o ano de nascimento da pessoa {i+1}: "))
    idade = atual - nascimento
    if idade >= 18:
        maiores += 1
    else:
        menores += 1

print(f"{maiores} pessoas já são maiores de idade.")
print(f"{menores} pessoas ainda não atingiram a maioridade.")
