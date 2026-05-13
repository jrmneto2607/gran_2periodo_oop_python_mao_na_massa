from classes.Produto import Produto
from classes.Categoria import Categoria

def menu():
    print()
    print('1 - Listar produtos')
    print('2 - Inserir produto')
    print('3 - Alterar produto')
    print('4 - Excluir produto')
    print('0 - Sair')
    print()

opcao = 1

while opcao != 0:
    menu()
    opcao = int(input('Digite a opção desejada: '))

    match opcao:
        case 1:
            Produto.listar_todos()
        case 2:
            codigo = input('Digite o código do produto: ')
            nome = input('Digite o nome do produto: ')
            quantidade = input('Digite a quantidade do produto: ')
            valor = input('Digite o valor do produto: ')

            produto = Produto(codigo, nome, quantidade, valor)
            produto.inserir()
        case 3:
            Produto.listar_todos()
            print()
            selecionado = int(input('Digite o número do produto que deseja alterar: '))
            item = Produto.consultar(selecionado)

            quantidade = input('Digite a quantidade do produto: ')
            valor = input('Digite o valor do produto: ')

            produto = Produto(item['codigo'], item['nome'], quantidade, valor)
            produto.alterar(selecionado)
        case 4:
            Produto.listar_todos()
            print()
            selecionado = int(input('Digite o número do produto que deseja excluir: '))

            Produto.excluir(selecionado)