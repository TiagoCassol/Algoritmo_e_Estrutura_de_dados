from ContaBancaria import ContaBancaria
 
class ContaCorrente(ContaBancaria):
    def __init__(self,nome,saldo,limite, tarifaMensal):
        super().__init__(nome,saldo,limite)
        self.tarifaMensal = tarifaMensal

    def cadastrar(self,nome, saldo,limite,tarifaMensal):
        self.nome = nome
        self.saldo = saldo
        self.limite = limite
        self.tarifaMensal = tarifaMensal

    def depositar(self,saldo):
         self.saldo += saldo
    
    def imprimir(self):
        print("Conta Corrente")
        super().imprimir()
        print("Tarifa Mensal: ",self.tarifaMensal)