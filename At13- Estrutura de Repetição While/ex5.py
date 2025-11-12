sexo = input("Informe o sexo (M/F): ").strip().upper()
while sexo not in ('M', 'F'):
    print("Valor inválido. Digite novamente.")
    sexo = input("Informe o sexo (M/F): ").strip().upper()
print(f"Sexo registrado: {sexo}")
