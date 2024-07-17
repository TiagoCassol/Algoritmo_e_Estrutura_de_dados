from Apartamento import Apartamento

class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def add(self, ap):
        # Adiciona um novo apartamento à fila
        if self.inicio == None:
            # Se a fila está vazia, o novo apartamento é o primeiro elemento
            self.inicio = ap
        else:
            # Se a fila não está vazia, adiciona o novo apartamento no final
            self.fim.proximo = ap
        # Atualiza o fim da fila para o novo apartamento
        self.fim = ap
        self.tamanho += 1
        self.imprimir()

    def imprimir(self):
        if self.inicio == None:
            print( "Fila Vazia ")
        else:
            print( "Fila de espera")
            aux = self.inicio
            texto = ""
            while( aux ):
                texto += str(aux.numero) + ": "
                texto += aux.torre.nome + " \n" 
                aux = aux.proximo
            print( texto )
            print( "Total: " , self.tamanho )

    def remover(self, nVaga):
        # Remove o primeiro apartamento da fila e o atribui uma vaga
        if self.inicio == None:
            print( "Fila Vazia" )
        else:
            # Se a fila contém apenas um apartamento
            if self.inicio.proximo == None:
                self.fim = None
            # Atribui a vaga ao primeiro apartamento
            self.inicio.vaga = nVaga
            # Guarda o primeiro apartamento
            ap = self.inicio
            # Move o início da fila para o próximo apartamento
            self.inicio = self.inicio.proximo
            # Diminui o tamanho da fila em um
            self.tamanho -= 1
            # Imprime o estado atual da fila
            self.imprimir()
            # Remove a referência ao próximo apartamento do removido
            ap.proximo = None
            # Retorna o apartamento removido
            return ap