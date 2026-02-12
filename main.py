#Nome: Nicholas Gabriel Silva Soares
#Data: 12/02/26
#Tema: Sistema de caixa de Supermercado e Controle de Estoque


#Bibliotecas
import json
import os

#Variavél para os arquivos Json
arquivo_estoque = "produtos.json"
arquivo_nota = "nota.json"

#Arquivo -------------------------------------------
def carregar_arquivo(nome_arquivo):
    if os.path.exists(nome_arquivo):
        with open(nome_arquivo, "r") as f:
            return json.load(f)
    return {}


def salvar_arquivo(nome_arquivo, dados):
    with open(nome_arquivo, "w") as f:
        json.dump(dados, f, indent=4)


#Estoque ------------------------------------------
def exibir_estoque(estoque):
    if not estoque:
        print("\n⚠ Estoque vazio!")
        return

    print("\n======= ESTOQUE =======")
    for codigo, dados in estoque.items():
        print(f"\nCódigo: {codigo}")
        print(f"Nome: {dados['nome']}")
        print(f"Preço: R${dados['preco']:.2f}")
        print(f"Quantidade: {dados['quantidade']}")
        print("-" * 30)


#Função do Gerente de Controle do Estoque ===================
def adicionar_estoque(estoque):
    codigo = input("Código do produto: ")

    #Se o codigo informado ja existir:
    if codigo in estoque:
        print("Produto já existe!")
        return

    #Adicionar o Produto
    nome = input("Nome do produto: ")
    preco = float(input("Preço: "))
    quantidade = int(input("Quantidade: "))

    estoque[codigo] = {
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }

    #Salva no arquivo
    salvar_arquivo(arquivo_estoque, estoque)
    print("Produto adicionado ao estoque!")

#Função do Gerente para remover do estoque
def remover_estoque(estoque):
    codigo = input("Código do produto a remover: ")

    #Se o codigo selecionado estiver no estoque:
    if codigo in estoque:
        del estoque[codigo]
        salvar_arquivo(arquivo_estoque, estoque)
        print("Produto removido do estoque!")
    else:
        print("Produto não encontrado!")



#Caixa ----------------------------------------------

#O caixa adiciona o produto do cliente na nota
def adicionar_na_nota(estoque, nota):
    codigo = input("Código do produto: ")

    if codigo not in estoque:
        print("Produto não encontrado no estoque!")
        return

    quantidade = int(input("Quantidade: "))

    if quantidade > estoque[codigo]["quantidade"]:
        print("Estoque insuficiente!")
        return

    produto = estoque[codigo]

    # Se já estiver na nota, soma quantidade
    if codigo in nota:
        nota[codigo]["quantidade"] += quantidade
    else:
        nota[codigo] = {
            "nome": produto["nome"],
            "preco": produto["preco"],
            "quantidade": quantidade
        }

    # O sistema atualiza a quantidade do Estoque
    estoque[codigo]["quantidade"] -= quantidade
    #Salva alterações nos arquivos Json
    salvar_arquivo(arquivo_estoque, estoque)
    salvar_arquivo(arquivo_nota, nota)

    print("Produto adicionado à nota!")

#O caixa remove o produto da nota
def remover_da_nota(estoque, nota):
    codigo = input("Código do produto a remover da nota: ")

    #Se o codigo pedido estiver na nota:
    if codigo in nota:
        quantidade = nota[codigo]["quantidade"]

        # Devolve ao estoque
        estoque[codigo]["quantidade"] += quantidade

        #Remove da nota
        del nota[codigo]

        #Salva o arquivo atualizado
        salvar_arquivo(arquivo_estoque, estoque)
        salvar_arquivo(arquivo_nota, nota)

        print("Produto removido da nota!")
    else:
        print("Produto não está na nota!")

#Gera a nota do cliente
def gerar_nota(nota):

    #Se a nota não existir:
    if not nota:
        print("\nNenhum item na nota!")
        return


    total = 0
    print("\n========= NOTA FISCAL =========")

    #Formatação da nota ===============================
    for dados in nota.values():
        subtotal = dados["preco"] * dados["quantidade"]
        total += subtotal
        print(f"{dados['nome']} - {dados['quantidade']} x R${dados['preco']:.2f} = R${subtotal:.2f}")

    print("-" * 35)
    print(f"TOTAL: R${total:.2f}")
    print("=" * 35)
    #==================================================

#Finaliza a compra do cliente
def finalizar_compra():

    #Reescreve o arquivo da nota
    salvar_arquivo(arquivo_nota, {})
    print("\nCompra finalizada!")
    print("Nota limpa para próxima compra.")



#Menu do Sistema =============================================
def menu():
    while True:
        estoque = carregar_arquivo(arquivo_estoque)
        nota = carregar_arquivo(arquivo_nota)

        print('\n' + '{:=^50}'.format(' BAESSE STORE '))
        print("""
[ 1 ] Exibir estoque
[ 2 ] Adicionar produto ao estoque (Gerente)
[ 3 ] Remover produto do estoque (Gerente)
[ 4 ] Adicionar produto à nota (Caixa)
[ 5 ] Remover produto da nota
[ 6 ] Gerar nota fiscal
[ 7 ] Finalizar compra
[ 8 ] Sair
""")

        try:
            opcao = int(input(">> Escolha uma opção: "))

            if opcao == 1:
                exibir_estoque(estoque)

            elif opcao == 2:
                adicionar_estoque(estoque)

            elif opcao == 3:
                remover_estoque(estoque)

            elif opcao == 4:
                exibir_estoque(estoque)
                adicionar_na_nota(estoque, nota)

            elif opcao == 5:
                remover_da_nota(estoque, nota)

            elif opcao == 6:
                gerar_nota(nota)

            elif opcao == 7:
                gerar_nota(nota)
                finalizar_compra()

            elif opcao == 8:
                print("Encerrando sistema...")
                break

            else:
                print("Opção inválida!")

        except ValueError:
            print("Digite apenas números!")
#=============================================================


#Execução
if __name__ == "__main__":
    menu()
