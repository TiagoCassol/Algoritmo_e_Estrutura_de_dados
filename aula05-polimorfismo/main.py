from Categoria import Categoria
from Veiculo import Veiculo
from Carro import Carro
from Moto import Moto


cat1 = Categoria()
cat2 = Categoria("esportiva")

v1 = Veiculo()
v1.imprimir()
print("--------------------------")

c1 = Carro("jeep",2021 ,Categoria("SUV"),4)
c1.imprimir()
print("--------------------------")

m1 = Moto("honda", 2020, cat2, 250)
m1.imprimir()