import matplotlib.pyplot as plt
from moedas import get_cotacao

cotacoes = get_cotacao()

l_moedas = ['USD - Dólar', 'EUR - Euro', 'GBP - Libras']
l_valores = [1 / cotacoes['USD'], 1 / cotacoes['EUR'], 1 / cotacoes['GBP']]

def grafico_de_barra(l_moedas, l_valores):
    plt.bar(l_moedas, l_valores)
    plt.title('Conversões para Real (BRL)')
    plt.xlabel('Moedas')
    plt.ylabel('BRL (R$)')
    plt.show()

def grafico_de_pizza(l_moedas, l_valores):
    plt.pie(l_valores, labels=l_moedas)
    plt.title('Proporção em relação ao Real Brasileiro (BRL)')
    plt.show()

def grafico_de_dispersao(l_moedas, l_valores):
    plt.scatter(l_moedas, l_valores)
    plt.title('Conversões para Real (BRL)')
    plt.xlabel('Moedas')
    plt.ylabel('BRL (R$)')
    plt.show()

def menu():
    print()
    print('1 - Gráfico de Barra')
    print('2 - Gráfico de Pizza')
    print('3 - Gráfico de Dispersão')
    print('0 - Sair')
    print()

if __name__ == "__main__":
    opcao = 1
    while opcao != 0:
        menu()
        try:
            opcao = int(input("Escolha uma opção: "))

            match opcao:
                case 1:
                    grafico_de_barra(l_moedas, l_valores)
                case 2:
                    grafico_de_pizza(l_moedas, l_valores)
                case 3:
                    grafico_de_dispersao(l_moedas, l_valores)
                case 0:
                    print("Saindo...")
        except ValueError:
            print("Opção inválida. Por favor, escolha um número válido.")