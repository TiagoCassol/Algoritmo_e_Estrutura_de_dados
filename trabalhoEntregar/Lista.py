from Apartamento import Apartamento

class Lista:
    def __init__(self):
        self.inicio = None
        self.tamanho = 0
        
    def add(self, ap):
        # Se a lista está vazia, o novo apartamento é adicionado como o primeiro elemento
        if self.inicio == None:
            self.inicio = ap
        else:
             # Se a vaga do novo apartamento é menor que a vaga do primeiro elemento,
             # o novo apartamento se torna o primeiro elemento da lista
            if ap.vaga < self.inicio.vaga:
                ap.proximo = self.inicio
                self.inicio = ap
            else:
                 # Caso contrário, percorre a lista para encontrar a posição correta para o novo apartamento
                ant = self.inicio
                aux = self.inicio.proximo
                while aux != None :
                    # Se encontrar uma vaga maior, insere o novo apartamento antes desse elemento
                    if ap.vaga < aux.vaga:
                        ap.proximo = ant.proximo   
                        ant.proximo = ap
                        break
                    else: 
                        # Continua percorrendo a lista
                        ant = aux
                        aux = aux.proximo
                 # Se o novo apartamento tem a maior vaga, é adicionado ao final da lista
                if aux == None and ap.vaga >= ant.vaga:
                    ant.proximo = ap
        # Incrementa o tamanho da lista
        self.tamanho += 1
        self.imprimir()
                            
    def imprimir(self):
        print("---------------------")
        if self.inicio == None:
            print("Lista Vazia!")
        else:
            print("Lista de Apartamentos")
            # Inicializa um ponteiro auxiliar para percorrer a lista
            aux = self.inicio
            # Percorre todos os elementos da lista
            while aux :
                # Imprime a representação do apartamento atual
                print( aux )
                # Move para o próximo apartamento na lista
                aux = aux.proximo
                print("--------------")
            print( "Quantidade de vagas: ", str(self.tamanho))
            
    def remover(self, vaga):
        # Guarda o tamanho atual da lista para comparar mais tarde
        tamAtual = self.tamanho
        # Se a lista estiver vazia, imprime uma mensagem e sai da função
        if self.inicio == None:
            print("Lista Vazia")
        # Se a lista contiver apenas um elemento e for o que queremos remover
        elif self.inicio.proximo == None and self.inicio.vaga == vaga:
            # Guarda o apartamento a ser removido
            ap = self.inicio
            # Define o início da lista como vazio
            self.inicio = None
            # Define o tamanho da lista para zero
            self.tamanho = 0
            # Retorna o apartamento removido
            return ap
        else:
            # Lista contendo vários elementos e o valor é igual ao primeiro
            if self.inicio.vaga == vaga:
                ap = self.inicio
                self.inicio = self.inicio.proximo
                self.tamanho -= 1
                print(ap)
                return ap
            # Se o elemento a ser removido não estiver no início da lista   
            else:
                ant = self.inicio
                aux = self.inicio.proximo
                 # Percorre a lista até encontrar o elemento ou chegar ao final
                while aux :
                    if aux.vaga == vaga:
                        ant.proximo = aux.proximo
                        self.tamanho -= 1
                        print(aux)
                        return aux
                    else:
                        ant = aux
                        aux = aux.proximo
        if tamAtual == self.tamanho:
            print("Valor não encontrado")
            return None
        self.imprimir()
                
                
            