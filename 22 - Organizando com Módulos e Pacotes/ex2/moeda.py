def aumentar(dados, chave, valor_a_aumentar):
    if chave in dados:
        dados[chave] += valor_a_aumentar
    else:
        dados[chave] = valor_a_aumentar
    return dados

def diminuir(dados, chave, valor_a_diminuir):
    if chave in dados:
        dados[chave] -= valor_a_diminuir
        if dados[chave] < 0:
            dados[chave] = 0
    return dados

def dobrar(dados, chave):
    if chave in dados:
        dados[chave] *= 2
    return dados

def mostrar(dados):
    """
    Mostra os valores dos dados com formatação monetária (R$).
    """
    print("=== Metadados Atualizados ===")
    for chave, valor in dados.items():
        if isinstance(valor, (int, float)):
            valor_formatado = f"R$ {valor:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
            print(f"{chave}: {valor_formatado}")
        else:
            print(f"{chave}: {valor}")
    print("==============================")
