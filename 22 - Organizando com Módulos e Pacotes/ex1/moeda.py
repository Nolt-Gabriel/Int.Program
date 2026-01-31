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
