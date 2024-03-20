from Cidade import Cidade
from Pessoa import Pessoa
from Pedido import *

c1 = Cidade("POA")

p1 = Pessoa("João")
p2 = Pessoa("Maria")



print("-----------------------")
c2 = Cidade()
c3 = Cidade("Capão da Canoa")

p3 = Pessoa("julia")
p4 = Pessoa("carlos",28)
p5 = Pessoa("suzy",40, c2)

print("-----------------------")

ca1=Categoria("refrigerante")
ca2=Categoria("sucos")

pr1=Produto("coca-cola",5,5,ca1)
pr2=Produto("del-vale",10,9,ca2)

pe1=Pedido("poa",pr1,p5)

print(pe1)


