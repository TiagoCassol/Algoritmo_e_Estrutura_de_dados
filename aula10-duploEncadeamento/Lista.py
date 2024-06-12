from No import No

class Lista:
        def __init__(self):
                self.inicio = None
                self.tamanho = 0
                self.fim = None

        
        def adicionarNoInicio(self, valor):
                nodo = No(valor)
                if self.inicio:
                        nodo.proximo = self.inicio
                self.inicio = nodo
                self.tamanho += 1
                self.imprimir()


        def adicionarNoFim(self,valor):
                nodo = No(valor)
                if self.inicio == None:
                        self.inicio = nodo
                else:
                        aux = self.inicio
                        while aux.proximo:
                                aux = aux.proximo
                        aux.proximo = nodo
                self.tamanho += 1
                self.imprimir()
        
        def imprimir(self):
                print("--------Lista Encadeada-------")
                if self.inicio == None:
                        print("Lista vazia")
                else:
                        print(self.tamanho, "elementos na lista")
                        aux = self.inicio
                        while aux:
                                print(aux.dado)
                                aux = aux.proximo

        def imprimirInverso(self):
                print("--------Lista Encadeada Inversa-------")
                if self.inicio == None:
                        print("Lista vazia")
                else:
                        print(self.tamanho, "elementos na lista")
                        aux = self.fim
                        while aux:
                                print(aux.dado)
                                aux = aux.anterior


        def adicionarOrdenado(self, valor):
            nodo = No(valor)
            #verefica se a lista esta vazia ou se o inicio é maior que valor do nodo
            if self.inicio is None or self.inicio.dado > valor:
                nodo.proximo = self.inicio
                self.inicio = nodo
                #se tiver apenas um elemento na lista o final da lista recebera o Nodo(o elemento)
                if self.inicio.proximo is None:
                        self.fim = nodo
            else:
                aux = self.inicio
                #fica no while até achar seu lugar
                while aux.proximo and aux.proximo.dado < valor:
                    aux = aux.proximo
                #se chegar no final da lista
                if aux.proximo is None:
                        #insere nodo no final da lista
                        aux.proximo = nodo
                        nodo.anterior = aux
                        self.fim = nodo
                else:
                        #insere nodo no meio da lista
                        nodo.proximo = aux.proximo
                        nodo.anterior = aux
                        aux.proximo.anterior = nodo
                        aux.proximo = nodo
            self.tamanho += 1

        def removerDoInicio(self):
                if self.inicio:
                        self.inicio = self.inicio.proximo
                        self.tamanho -= 1
                self.imprimir()

        def removerDoFim(self):
                if self.inicio:
                        if self.inicio.proximo == None:
                                self.inicio = None
                        else:
                                anterior = self.inicio
                                aux = self.inicio.proximo
                                while aux.proximo:
                                        anterior = aux
                                        aux = aux.proximo
                                anterior.proximo = None
                        self.tamanho -= 1
                self.imprimir()