from Apartamento import Apartamento
from Torre import Torre
# 1) Construa a classe Torre e a classe Apartamento. A classe Torre deve possuir os atributos id, nome e endereço. A classe Apartamento deve conter os atributos, id, número 
# do apartamento, número da vaga de garagem e torre.

Torre = Torre("teste","rrr")
Apartamento = Apartamento()

Torre.imprimir()
Apartamento.imprimir()
# Apartamento.imprimir()

# Apartamento.add("joão")
# Apartamento.add("maria")
# Apartamento.add("julia")

# Apartamento.remover()
 

# 2) Este condomínio, não possui vagas de garagem para todos os apartamentos. Isso faz com que exista uma fila de espera por vagas. Implemente uma fila de espera que 
# contenha os métodos para adicionar apartamentos na fila, retirar apartamentos informando o número da vaga que este apartamento receberá e um método para imprimir a fila de espera.





# 3) O condomínio tem apenas 10 vagas de garagem. Então, no monento que o décimo primeiro apartamento for cadastrado, este apartamento deve ir para a fila de espera. 
# Os apartamento que tem vaga de garagem, devem ficar na lista encadeada de apartamento com vaga, ordenados pelo número da vaga.

