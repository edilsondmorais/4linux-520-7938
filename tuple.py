## Tuple é imutável, porém pode ser alterado o conteúdo exemplo em lista nesta tuple

dados = ('Edilson', 42, 'CI&T')

print(dados[0])
print(dados[1])
print(dados[2])

for dado in dados:
    print(f"dado é {dado}")

nome, idade, trabalho = dados
print(f"nome:   {nome}")
print(f"Idade:   {idade}")
print(f"Trabalho:   {trabalho}")

(cidade, estado, pais) = ('SAO PAULO', 'SP', 'Brasil')
print(cidade, estado, pais)

print(dados.count(29))
print(dados.index('CI&T'))

turma = (520, 7938, ['Edilson'])
turma[2].append('Morais') ## Só é possível modificar a lista que contém na tuple
print(turma)