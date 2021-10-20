
string = input ("Digite qualquer palavra: ")

for i in string:
    if i.islower():  # i == i.upper é a mesma coisa
        print(f"caractere {i} é minuscula")

    elif i.isupper():
        print(f"caractere {i} é maiuscula")

    elif i.isnumeric():
        print(f"caractere {i} é Numero")

    else:
        print(f"caractere {i} é qualquer outra coisa!!")