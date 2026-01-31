def aumentar(valor, aumento, formato=False):
    
    novo_valor = valor + aumento
    if formato == 'M':
        novo_valor = formatar(novo_valor)
    print(f"Aumentando em R$ {aumento:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.'))
    print(f"Novo valor: {novo_valor}")
    print()
    return novo_valor

def diminuir(valor, reducao, formato=False):
    
    novo_valor = valor - reducao
    if novo_valor < 0:
        novo_valor = 0
    if formato == 'M':
        novo_valor = formatar(novo_valor)
    print(f"Diminuindo em R$ {reducao:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.'))
    print(f"Novo valor: {novo_valor}")
    print()
    return novo_valor

def dobrar(valor, formato=False):
    
    novo_valor = valor * 2
    if formato == 'M':
        novo_valor = formatar(novo_valor)
    print("Dobhando o valor!")
    print(f"Novo valor: {novo_valor}")
    print()
    return novo_valor

def formatar(valor):
    
    return f"R$ {valor:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
