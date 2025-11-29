from datetime import date

pessoa = {}

ano_atual = date.today().year

pessoa["nome"] = input("Nome: ")
nasc = int(input("Ano de nascimento: "))
pessoa["idade"] = ano_atual - nasc
pessoa["ctps"] = int(input("Carteira de trabalho (0 se não tem): "))

if pessoa["ctps"] != 0:
    pessoa["ano_contratacao"] = int(input("Ano de contratação: "))
    pessoa["salario"] = float(input("Salário: R$ "))

    anos_trabalho = (pessoa["ano_contratacao"] + 35) - ano_atual
   
    pessoa["aposentadoria"] = pessoa["idade"] + anos_trabalho

print("-=" * 30)
for k, v in pessoa.items():
    print(f"{k.capitalize()}: {v}")
