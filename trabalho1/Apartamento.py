class Apartamento:
    def __init__(self, id, numero, torre, vaga=None, proximo=None):
        self.id = id
        self.numero = numero
        self.vaga = vaga
        self.torre = torre
        self.proximo = proximo

    def cadastrar(self):
        print(f'Apartamento {self.numero} cadastrado com sucesso!')

    def imprimir(self):
        print(f'ID: {self.id}')
        print(f'Número: {self.numero}')
        print(f'Vaga: {self.vaga if self.vaga else "Nenhuma"}')
        print(f'Torre: {self.torre.nome if self.torre else "Nenhuma"}')
        if self.proximo:
            print(f'Próximo Apartamento: {self.proximo.numero}')
        else:
            print('Próximo Apartamento: Nenhum')
