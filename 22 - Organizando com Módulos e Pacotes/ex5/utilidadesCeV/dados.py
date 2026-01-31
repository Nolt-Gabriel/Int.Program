from .moeda import formatar

def mostrar(dados):
   
    print("=== Dados Atualizados ===")
    for chave, valor in dados.items():
        print(f"{chave}: {formatar(valor) if isinstance(valor, (int, float)) else valor}")
    print("==========================")

def leiaDinheiro(msg):
   
    while True:
        entrada = input(msg).strip().replace(',', '.')
        try:
            valor = float(entrada)
            if valor < 0:
                print("ERRO: Valor monetário não pode ser negativo!")
                continue
            return valor
        except ValueError:
            print("ERRO: Digite um valor monetário válido (ex: 1500.50 ou 1.500,50)!")
