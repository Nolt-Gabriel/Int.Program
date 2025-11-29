expressao = input("Digite uma expressão: ")

pilha = []

for simbolo in expressao:
    if simbolo == "(":
        pilha.append("(")          # abre: empilha
    elif simbolo == ")":
        if len(pilha) > 0:
            pilha.pop()            # fecha: desempilha um
        else:
            pilha.append(")")      # fechou sem ter aberto
            break

if len(pilha) == 0:
    print("Expressão válida (parênteses corretos).")
else:
    print("Expressão inválida (parênteses incorretos).")
