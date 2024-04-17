from Carro import Carro
from Moto import Moto
from ContaCorrente import ContaCorrente
from ContaPoupanca import ContaPoupanca

c1 = Carro("Renegade", 2021,4)
c1.ligar("1234")
c1.imprimir()
c1.desligar()
print("\n--------------------------------------\n")
m1 = Moto("twister",2020,250)
m1.ligar("123")
m1.imprimir()
m1.desligar()
print("\n--------------------------------------\n")
cc = ContaCorrente("dada",200,1000,2)
cc.cadastrar("dadaaaa",2001,1000,2)
cc.depositar(30)
cc.imprimir()
print("\n--------------------------------------\n")
cp = ContaPoupanca("dasdad",333,5000,0.1)
cp.cadastrar("dasdad",333,5000,0.1)
cp.depositar(100)
cp.imprimir()