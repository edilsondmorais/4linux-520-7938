somar=lambda x, y: x + y
subtrair=lambda x, y: x - y
dividir=lambda x, y: x / y
multiplicar=lambda x, y: x * y

opcao_valida = [0,1,2,3,4]
operacoes = ["somar","subtrair","multiplicar","dividir","Sair"]

while True:
    try:
        for (i,o) in enumerate(operacoes):
            print(f'{i} - {o}')

        opcao = int(input("Oscolha a operaçao: "))
        print()

        if opcao not in opcao_valida:
            print("Digite uma opção válida !!!",end='\n\n')
            continue
        elif opcao == 4:
            print("Até logo, volte sempre!!!")
            break
        x = int(input("Digite o primeiro número: "))
        y = int(input("Digite o segundo número: "))

        if opcao == 0:
            print("Resultado= ",somar(x, y))
            print()
        elif opcao == 1:
            print("Resultado= ",subtrair(x, y))
            print()
        elif opcao == 2:
            print("Resultado= ",multiplicar(x, y))
            print()
        elif opcao == 3:
            print("Resultado= ",dividir(x, y))
            print()
    except ZeroDivisionError as ZD:
        print("Zero não é divizível!!!",end='\n\n')
    except ValueError as VE:
        print("O caracter digitado não é válido!!!",end='\n\n')
    else:
        print("Calculo realizado com sucesso!!!",end='\n\n')