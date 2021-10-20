#string = 'sequencia de caracteres'
#
#for caractere in string:
#    print(caractere)

#for i in range(1, 11): ## o Valor de inicio é inclusivo e o de fim é exclusivo
#    print(i)

#for i in range(10, -1, -1): ## Contagem regressiva, tb o Valor de inicio é inclusivo e o de fim é exclusivo
#    print(i)

for i in range(10):
    if i % 3 == 0:
        continue
    if i % 2 == 0:
        print(i)
    if i % 2 == 0:
        break
else: ## Só entra no else se ele terminar o loop do for, caso ele quebre no break ele não entrarar no else;
    print('Fora do loop!')