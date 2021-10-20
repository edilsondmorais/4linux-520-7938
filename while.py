valor = 10

#while valor > 0:
#    print("Valor: ", valor)
#    valor -= 1
#
#print("Fora do loop")
#
while valor > 0:
    valor -= 1
    if valor % 2 != 0:
        continue ## Faz voltar para o inicio do while
    print("Valor: ", valor)

    if valor == 0: ## Faz sair do loop
        break

else:   ## Só entra no else se ele terminar o loop do while, caso ele quebre no break ele não entrarar no else;
    print("Fim do loop")

print("Fora do loop!! UFA!")