import json

class AbstractCrud:
    def detalhar(self):
        return self.__dict__

    def inserir(self):
        lista = self.consultar()
        lista.append(self.detalhar())
        
        self.__gravar_arquivo(lista)
        print(f'inserido com sucesso!')

    
    def alterar(self, item):
        lista = self.consultar()
        lista[item] = self.detalhar()

        self.__gravar_arquivo(lista)
        print(f'alterado com sucesso!')


    @classmethod
    def excluir(cls, item):
        lista = cls.consultar()
        del lista[item]

        cls.__gravar_arquivo(cls, lista)
        print(f'excluído com sucesso!')



    def __gravar_arquivo(self, lista):
        with open(self.arquivo, 'w') as file:
            json.dump(lista, file, indent=4)


    @classmethod
    def listar_todos(cls):
        lista = cls.consultar()
        
        for index, item in enumerate(lista):
            print(f'{index} - {item}')
    
    @classmethod
    def consultar(cls, item = None):
        try:
            with open(cls.arquivo) as file:
                lista = json.load(file)
                return lista if item is None else lista[item]
        except Exception as e:
            return []