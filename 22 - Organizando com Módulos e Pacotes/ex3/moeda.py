def aumentar(dados, chave, aumento, formato=False):
    if chave in dados:
        dados[chave] += aumento
    else:
        dados[chave] = aumento
    
    valor_retorno = dados[chave]
    if formato == 'M':
        valor_retorno = formatar(valor_retorno)
    
    print(f"Aumentando {chave} em R$ {aumento:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.'))
    print(f"Novo {chave}: {valor_retorno}")
    print()
    return dados

def diminuir(dados, chave, reducao, formato=False):
    if chave in dados:
        dados[chave] -= reducao
        if dados[chave] < 0:
            dados[chave] = 0
    
    valor_retorno = dados[chave]
    if formato == 'M':
        valor_retorno = formatar(valor_retorno)
    
    print(f"Diminuindo {chave} em R$ {reducao:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.'))
    print(f"Novo {chave}: {valor_retorno}")
    print()
    return dados

def dobrar(dados, chave, formato=False):
    if chave in dados:
        dados[chave] *= 2
    
    valor_retorno = dados[chave]
    if formato == 'M':
        valor_retorno = formatar(valor_retorno)
    
    print(f"Dobrando {chave}!")
    print(f"Novo {chave}: {valor_retorno}")
    print()
    return dados

def formatar(valor):
    
    return f"R$ {valor:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')

def mostrar(dados):
    print("=== Dados Atualizados ===")
    for chave, valor in dados.items():
        print(f"{chave}: {formatar(valor) if isinstance(valor, (int, float)) else valor}")
    print("==============================")
