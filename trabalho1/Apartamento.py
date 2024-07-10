#pip install colorama
from colorama import Fore, Style, init

# Inicializa a biblioteca colorama
init(autoreset=True)
class Apartamento:
    def __init__(self, id, numero, torre, vaga=None, proximo=None):
        self.id = id
        self.numero = numero
        self.vaga = vaga
        self.torre = torre
        self.proximo = proximo # Próximo apartamento na lista encadeada

    def cadastrar(self):
        print(f'Apartamento {self.numero} cadastrado com sucesso!')

    def imprimir(self):
        print(Fore.YELLOW + Style.BRIGHT + '------------------------------')
        print(Fore.WHITE + Style.BRIGHT + f'ID: {self.id}')
        print(Fore.WHITE + Style.BRIGHT + f'Número: {self.numero}')
        print(Fore.WHITE + Style.BRIGHT + f'Vaga: {self.vaga if self.vaga else "Nenhuma"}')
        print(Fore.WHITE + Style.BRIGHT + f'Torre: {self.torre.nome if self.torre else "Nenhuma"}')
        if self.proximo:
            print(f'Próximo Apartamento: {self.proximo.numero}')
        else:
            print('Próximo Apartamento: Nenhum')
        print(Fore.YELLOW + Style.BRIGHT + '------------------------------')
