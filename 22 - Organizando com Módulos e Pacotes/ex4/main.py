from utilidadesCeV import aumentar, diminuir, dobrar, mostrar

# Testando com dicionário de dados
dados = {"túnel": 1500.0}

# Usando as funções transferidas (funcionam igual!)
dados["túnel"] = aumentar(dados["túnel"], 1000, formato='M')
dados["túnel"] = diminuir(dados["túnel"], 500, formato='M')
dados["túnel"] = dobrar(dados["túnel"], formato='M')

mostrar(dados)
