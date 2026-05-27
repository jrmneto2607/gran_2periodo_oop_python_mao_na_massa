from moedas import converter_cotacao


def menu():
    print()
    print('1 - Converter Dollar em Real')
    print('2 - Converter Euro em Real')
    print('3 - Converter Libras em Real')
    print('4 - Outra cotação')
    print('0 - Sair')
    print()


if __name__ == "__main__":
    opcao = 1
    while opcao != 0:
        menu()
        opcao = int(input("Escolha uma opção: "))
        valor = float(input("Digite o valor a ser convertido (ex: 10.00): "))
        origem = ""
        destino = "BRL"

        match opcao:
            case 1:
                origem = "USD"
            case 2:
                origem = "EUR"
            case 3:
                origem = "GBP"
            case 4:
                origem = input("Digite a moeda de origem: ")
                destino = input("Digite a moeda de destino: ")
            case 0:
                print("Saindo...")
                  
        if opcao in range(1, 5):
            print()
            print("*" * 30)          
            print(f"{origem} para {destino}: {converter_cotacao(origem, destino, valor)}")
            print("*" * 30)
            print()