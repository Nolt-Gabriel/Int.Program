from utilidadesCeV import aumentar, diminuir, dobrar, mostrar, leiaDinheiro

dados = {"preco": 0.0}


dados["preco"] = leiaDinheiro("Digite o preço do produto: R$ ")


dados["preco"] = aumentar(dados["preco"], 500, formato='M')
dados["preco"] = diminuir(dados["preco"], leiaDinheiro("Quanto desconto? R$ "), formato='M')
dados["preco"] = dobrar(dados["preco"], formato='M')

mostrar(dados)
