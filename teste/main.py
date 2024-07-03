class No:
    def __init__(self, valor):
        self.dado = valor
        self.proximo = None


class Torre:
    def __init__(self, id, nome, endereco):
        self.id = id
        self.nome = nome
        self.endereco = endereco

    def cadastrar(self):
        print(f'Torre {self.nome} cadastrada com sucesso!')

    def imprimir(self):
        print(f'ID: {self.id}')
        print(f'Nome: {self.nome}')
        print(f'Endereço: {self.endereco}')


class Apartamento:
    def __init__(self, id, numero, torre, vaga=None):
        self.id = id
        self.numero = numero
        self.vaga = vaga
        self.torre = torre

    def cadastrar(self):
        print(f'Apartamento {self.numero} cadastrado com sucesso!')

    def imprimir(self):
        print(f'ID: {self.id}')
        print(f'Número: {self.numero}')
        print(f'Vaga: {self.vaga if self.vaga else "Nenhuma"}')
        print(f'Torre: {self.torre.nome if self.torre else "Nenhuma"}')


class FilaEspera:
    def __init__(self):
        self.fila = []

    def adicionar_apartamento(self, apartamento):
        self.fila.append(apartamento)
        print(f'Apartamento {apartamento.numero} adicionado à fila de espera.')

    def retirar_apartamento(self, vaga):
        if self.fila:
            apartamento = self.fila.pop(0)
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
        self.apartamentos_com_vaga = None
        self.total_vagas = 3
        self.contador_apartamentos = 0
        self.fila_espera = FilaEspera()

    def cadastrar_apartamento(self, apartamento):
        self.contador_apartamentos += 1
        if self.total_vagas > 0:
            self.adicionar_com_vaga(apartamento)
        else:
            self.fila_espera.adicionar_apartamento(apartamento)

    def adicionar_com_vaga(self, apartamento):
        apartamento.vaga = 4 - self.total_vagas
        novo_no = No(apartamento)
        if self.apartamentos_com_vaga is None:
            self.apartamentos_com_vaga = novo_no
        else:
            atual = self.apartamentos_com_vaga
            anterior = None
            while atual and (atual.dado.vaga is None or atual.dado.vaga < apartamento.vaga):
                anterior = atual
                atual = atual.proximo
            novo_no.proximo = atual
            if anterior is None:
                self.apartamentos_com_vaga = novo_no
            else:
                anterior.proximo = novo_no
        self.total_vagas -= 1
        apartamento.cadastrar()

    def imprimir_com_vaga(self):
        if self.apartamentos_com_vaga:
            print('Apartamentos com vaga:')
            atual = self.apartamentos_com_vaga
            while atual:
                atual.dado.imprimir()
                atual = atual.proximo
        else:
            print('Nenhum apartamento com vaga.')

    def liberar_vaga(self, vaga):
        apartamento = self.apartamentos_com_vaga
        anterior = None
        while apartamento and apartamento.dado.vaga != vaga:
            anterior = apartamento
            apartamento = apartamento.proximo

        if apartamento:
            if anterior:
                anterior.proximo = apartamento.proximo
            else:
                self.apartamentos_com_vaga = apartamento.proximo
            apartamento.dado.vaga = None
            self.fila_espera.adicionar_apartamento(apartamento.dado)
            self.total_vagas += 1

        self.total_vagas -= 1
        apartamento_fila = self.fila_espera.retirar_apartamento(vaga)
        if apartamento_fila:
            self.adicionar_com_vaga(apartamento_fila)


# Exemplo de uso com menu
torre1 = Torre(1, 'Torre A', 'Endereço A')
condominio = Condominio()

while True:
    print("\nMenu:")
    print("a) Cadastrar apartamento")
    print("b) Liberar vaga")
    print("c) Imprimir a lista de apartamentos com vaga")
    print("d) Imprimir a fila de espera")
    print("e) Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == 'a':
        id = int(input("ID do apartamento: "))
        numero = input("Número do apartamento: ")
        apt = Apartamento(id, numero, torre1)
        condominio.cadastrar_apartamento(apt)
    elif opcao == 'b':
        vaga = int(input("Número da vaga a ser liberada: "))
        condominio.liberar_vaga(vaga)
    elif opcao == 'c':
        condominio.imprimir_com_vaga()
    elif opcao == 'd':
        condominio.fila_espera.imprimir_fila()
    elif opcao == 'e':
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")
