habilitado = input("Você é habilitado? ")

if habilitado.lower().startswith('sim'): ## O comando startswith aceita tudo q inicia com sim
    print("Você pode dirigir!")

else:
    print("Voce nao pode dirigir:")
