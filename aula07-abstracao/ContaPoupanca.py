from ContaBancaria import ContaBancaria
 
class ContaPoupanca(ContaBancaria):
    def __init__(self,nome,saldo,limite, taxaRendimento):
        super().__init__(nome,saldo,limite)
        self.taxaRendimento = taxaRendimento

    def cadastrar(self,nome, saldo,limite,taxaRendimento):
        self.nome = nome
        self.saldo = saldo
        self.limite = limite
        self.taxaRendimento = taxaRendimento

    def depositar(self,saldo):
         self.saldo += saldo
    
    def imprimir(self):
        print("Conta Poupança")
        super().imprimir()
        print("Taxa Rendimento: ",self.taxaRendimento)