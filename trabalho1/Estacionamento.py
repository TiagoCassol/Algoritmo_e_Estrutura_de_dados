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
        if self.apartamentos_com_vaga is None:
            self.apartamentos_com_vaga = apartamento
        else:
            atual = self.apartamentos_com_vaga
            anterior = None
            while atual and (atual.vaga is None or atual.vaga < apartamento.vaga):
                anterior = atual
                atual = atual.proximo
            apartamento.proximo = atual
            if anterior is None:
                self.apartamentos_com_vaga = apartamento
            else:
                anterior.proximo = apartamento
        self.total_vagas -= 1
        apartamento.cadastrar()

    def imprimir_com_vaga(self):
        if self.apartamentos_com_vaga:
            print('Apartamentos com vaga:')
            atual = self.apartamentos_com_vaga
            while atual:
                atual.imprimir()
                atual = atual.proximo
        else:
            print('Nenhum apartamento com vaga.')

    def liberar_vaga(self, vaga):
        apartamento = self.apartamentos_com_vaga
        anterior = None
        while apartamento and apartamento.vaga != vaga:
            anterior = apartamento
            apartamento = apartamento.proximo

        if apartamento:
            if anterior:
                anterior.proximo = apartamento.proximo
            else:
                self.apartamentos_com_vaga = apartamento.proximo
            apartamento.vaga = None
            self.fila_espera.adicionar_apartamento(apartamento)
            self.total_vagas += 1

        self.total_vagas -= 1
        apartamento_fila = self.fila_espera.retirar_apartamento(vaga)
        if apartamento_fila:
            self.adicionar_com_vaga(apartamento_fila)