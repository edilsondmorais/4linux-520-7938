import csv

def main():
    nome_arq = 'dados.csv'

    with open(nome_arq, 'r') as a:
        escrivao = csv.writer(a, delimiter=';')

        try:
            escrivao.writerow(['4444444444', 'Luis Potter', 20, 'H', 'Ingles'])
            escrivao.writerows([
                ['1234567890', 'Edilson SM', 40, 'H', 'Chines'],
                ['0987654321', 'Robin', '101', 'H', 'Gothanes']
            ])
        except IOError as UO:
            print("Arquivo aberto apenas para leitura, não é permitido escrita!!")


if __name__ == '__main__':
    main()