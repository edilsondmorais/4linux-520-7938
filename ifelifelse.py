habilitado = input("Você é habilitado? ").lower() ## Pode ser forcado a reduzir o tamanho aqui

if habilitado.startswith('s'): ## O comando startswith aceita tudo q inicia com sim
    print("Você pode dirigir!")
elif habilitado.startswith('n'): ## O elif pode ser utilizado quantas vezes quiser.
    print("Você nao pode dirigir!")

elif habilitado.find('s') != -1: ## Se encontrar o 's' em qualquer posição.
    print("Acho que Você pode dirigir!")

else:
    print("Nao entendi.")