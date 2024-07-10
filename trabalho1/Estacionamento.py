#pip install colorama
from colorama import Fore, Style, init

# Inicializa a biblioteca colorama
init(autoreset=True)

class No:
        def __init__(self, valor):
                self.dado = valor #armazena o valor do nodo
                self.proximo = None  #aponta para o proximo nodo da lista 

class FilaEspera:
    def __init__(self):
        self.fila = [] #fila de apartamentos da lista de espera

    def adicionar_apartamento(self, apartamento):
        self.fila.append(apartamento)
        print(f'Apartamento {apartamento.numero} adicionado à fila de espera.')

    def retirar_apartamento(self, vaga):
        # Verifica se há algum apartamento na fila de espera
        if self.fila:
            # Remove o primeiro apartamento da fila de espera (pop(0) remove e retorna o primeiro item da lista)
            apartamento = self.fila.pop(0)
            # Atribui a vaga especificada ao apartamento retirado da fila de espera
            apartamento.vaga = vaga
            print(f'Apartamento {apartamento.numero} retirado da fila e atribuído à vaga {vaga}.')
            return apartamento
        else:
            print('Fila de espera vazia.')
            return None

    def imprimir_fila(self):
        if self.fila:
            print('Fila de Espera:')
            for apartamento in self.fila:
                apartamento.imprimir()
        else:
            print('Fila de espera vazia.')


class Condominio:
    def __init__(self):
        self.apartamentos_com_vaga = None # Lista encadeada de apartamentos com vaga
        self.total_vagas = 10   # Número total de vagas de garagem disponíveis
        self.contador_apartamentos = 0 # Contador de apartamentos cadastrados
        self.fila_espera = FilaEspera()# Instância da classe FilaEspera para gerenciar a fila de espera


    def cadastrar_apartamento(self, apartamento):
        self.contador_apartamentos += 1
        if self.total_vagas > 0:
            self.adicionar_com_vaga(apartamento)
        else:
            self.fila_espera.adicionar_apartamento(apartamento)

    # Método para adicionar um apartamento à lista de apartamentos com vaga
    def adicionar_com_vaga(self, apartamento):
        if self.total_vagas > 0:
            # Calcula a vaga a ser atribuída ao apartamento
            apartamento.vaga = 11 - self.total_vagas
            # Caso especial: lista de apartamentos com vaga vazia
            if self.apartamentos_com_vaga is None:
                self.apartamentos_com_vaga = apartamento
                self.total_vagas -= 1
                apartamento.cadastrar()
                return
            atual = self.apartamentos_com_vaga
            anterior = None
            # Procura o lugar correto para inserir o apartamento na ordem crescente de vaga
            while atual and (atual.vaga is None or atual.vaga < apartamento.vaga):
                anterior = atual
                atual = atual.proximo
            # Insere o apartamento na posição correta da lista encadeada
            apartamento.proximo = atual
            if anterior is None:
                self.apartamentos_com_vaga = apartamento
            else:
                anterior.proximo = apartamento
            self.total_vagas -= 1
            apartamento.cadastrar()
        else:
            # Caso não haja mais vagas disponíveis
            self.fila_espera.adicionar_apartamento(apartamento)

    def imprimir_com_vaga(self):
        if self.apartamentos_com_vaga:
            print(Fore.GREEN + Style.BRIGHT + '==============================')
            print(Fore.CYAN + Style.BRIGHT + '   Apartamentos com Vaga   ')
            print(Fore.GREEN + Style.BRIGHT + '==============================')
            atual = self.apartamentos_com_vaga
            while atual:
                atual.imprimir()
                atual = atual.proximo
            print(Fore.GREEN + Style.BRIGHT + '==============================')
        else:
            print(Fore.RED + Style.BRIGHT + 'Nenhum apartamento com vaga.')


    def liberar_vaga(self, vaga):
        apartamento = self.apartamentos_com_vaga # Inicia a busca pelo apartamento com a vaga especificada a partir do primeiro da lista
        anterior = None
        # Encontra o apartamento com a vaga especificada
        while apartamento and apartamento.vaga != vaga:
            anterior = apartamento
            apartamento = apartamento.proximo
        if apartamento:
            # Remove a vaga do apartamento encontrado
            apartamento.vaga = None
            # Remove o apartamento da lista de apartamentos com vaga
            if anterior:
                anterior.proximo = apartamento.proximo
            else:
                self.apartamentos_com_vaga = apartamento.proximo
            # Adiciona o apartamento à fila de espera
            self.fila_espera.adicionar_apartamento(apartamento)
            # Incrementa o número total de vagas disponíveis
            self.total_vagas += 1

            # Ajusta a ordem na fila de espera, retirando o apartamento com a vaga especificada
            apartamento_fila = self.fila_espera.retirar_apartamento(vaga)
            if apartamento_fila:
                # Adiciona o apartamento retirado da fila de espera à lista de apartamentos com vaga
                self.adicionar_com_vaga(apartamento_fila)
        else:
            print('Vaga não encontrada.')

 