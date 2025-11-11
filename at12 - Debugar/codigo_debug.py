faturamento = 1000

def calcular_imposto(valor):
    imposto = valor * 0.3
    return imposto

imposto = calcular_imposto(faturamento)
print("Faturamento:", faturamento)
print("Imposto:", imposto)
print("Faturamento Líquido:", faturamento - imposto)