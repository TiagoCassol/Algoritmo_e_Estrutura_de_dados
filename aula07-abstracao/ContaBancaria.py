from abc import ABC, abstractmethod

class ContaBancaria(ABC):
    def __init__(self,nome,saldo,limite):
        self.nome = nome
        self.saldo = saldo
        self.limite = limite

    @abstractmethod
    def cadastrar(self,nome, saldo,limite):
        self.nome = nome
        self.saldo = saldo
        self.limite = limite

    @abstractmethod
    def depositar(self,saldo):
            self.saldo += saldo

    def imprimir(self):
        print("Nome: " , self.nome)
        print("Saldo: " , self.saldo)
        print("Limite: ", self.limite)

    def desligar(self):
        print("Veiculo desligado")