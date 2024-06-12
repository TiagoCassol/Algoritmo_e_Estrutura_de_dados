from No import No

class Fila:

    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def add(self, valor):
        nodo = No(valor)
        if self.inicio is None:
            self.inicio = nodo            
        else:
            self.fim.proximo = nodo
        self.fim = nodo
        self.tamanho +=1
        self.imprimir()

    def imprimir(self):
                print("--------Fila- FIFO-------")
                if self.inicio == None:
                        print("Fila vazia")
                else:
                        print(self.tamanho, "elementos na fila")
                        aux = self.inicio
                        texto = ""
                        while aux:
                            texto += aux.dado + " - "
                            aux = aux.proximo
                        print(texto)
            
    def remover(self):
            if self.inicio is not None:
                self.inicio = self.inicio.proximo
                if self.inicio == None:
                    self.fim = None
                self.tamanho -= 1
            self.imprimir()