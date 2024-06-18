from No import No

class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def add(self, placa, marca, cor):
        nodo = No(placa, marca, cor)
        if self.inicio is None:
            self.inicio = nodo
        else:
            self.fim.proximo = nodo
        self.fim = nodo
        self.tamanho += 1
        self.imprimir()

    def imprimir(self):
        print("--------Fila de Carros-------")
        if self.inicio is None:
            print("Fila vazia")
        else:
            print(self.tamanho, "elementos na fila")
            aux = self.inicio
            while aux:
                print(aux)
                aux = aux.proximo

    def lavar(self):
        if self.inicio is not None:
            self.inicio = self.inicio.proximo
            if self.inicio is None:
                self.fim = None
            self.tamanho -= 1
        self.imprimir()

