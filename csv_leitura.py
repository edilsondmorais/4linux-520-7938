import csv

def main():
    nome_arq = 'dados.csv'

    with open(nome_arq, 'w') as a:
        leitor = csv.reader(a, delimiter=';')

        try:
            for linha in leitor:
                print(linha)
        except IOError as UO:
            print("Arquivo aberto apenas para escrita, não é permitido leitura!!")


if __name__ == '__main__':
    main()