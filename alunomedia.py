nota1 = int ( input("Digite a primeira nota: "))
nota2 = int ( input("Digite a segunda nota: "))
nota3 = int ( input("Digite a terceira nota: "))

media = nota1 + nota2 + nota3 / 3

print(media)

if media > 6:
    print("Parabéns você foi aprovado!!!")

elif media >= 4:
    print("Você esta em recuperação!")

elif media < 4:
    print("Você repetiu!")

