from moeda import formatar

def mostrar(dados):

    print("=== Dados Atualizados ===")
    for chave, valor in dados.items():
        print(f"{chave}: {formatar(valor) if isinstance(valor, (int, float)) else valor}")
    print("==========================")
