telefone = {
    'Edilson': '011212121221',
    'Maisa' : '02666666888',
    'Adriana': '080808080808'
}

print(telefone)

for nome in telefone:
    print(nome, telefone[nome])

print(telefone['Edilson'])

print(telefone['Maisa'])

print(telefone['Adriana'])

for (nome, telefone) in telefone.items():
    print(f"Nome: {nome} Telefone: {telefone}")
