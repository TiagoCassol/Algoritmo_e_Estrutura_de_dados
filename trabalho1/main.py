from Apartamento import Apartamento
from Estacionamento import *
from Torre import Torre

# 1) Construa a classe Torre e a classe Apartamento. A classe Torre deve possuir os atributos id, nome e endereço. A classe Apartamento deve conter os atributos, id, número 
# do apartamento, número da vaga de garagem e torre.

torre1 = Torre(1, 'ttt', 'erondina')
condominio = Condominio()

for i in range(1, 6):
    apt = Apartamento(i, f'Apartamento {i}', torre1)
    condominio.cadastrar_apartamento(apt)

# 4) Construa um menu que permita ao usuário escolher as opções de:

# a) Cadastrar apartamento -> Quando o apartamento for cadastrado, se tiver vaga de garagem disponível, ele deve ir para a lista encadeada, ordenada pelo número da vaga. Se não 
# tiver mais vagas, o apartamento deve ir para a fila de apartamentos que estão esperando a vaga.

# b) Liberar vaga -> O Usuário deve informar o número da vaga que será liberada, então o apartamento que estiver nessa vaga deve ser colocado no fim da fila e o apartamento que 
# estiver no início da fila deve ir para a lista encadeada, assumindo a vaga de garagem que foi liberada.

# c) Imprimir a lista de apartamentos que tem vaga.

# d) Imprimir a fila de apartamentos que estão esperando por vaga de garagem.
while True:
    print("\nMenu:")
    print("1- Cadastrar apartamento")
    print("2- Liberar vaga")
    print("3- Imprimir a lista de apartamentos com vaga")
    print("4- Imprimir a fila de espera")
    print("5- Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        id = int(input("ID do apartamento: "))
        numero = input("Número do apartamento: ")
        apt = Apartamento(id, numero, torre1)
        condominio.cadastrar_apartamento(apt)
    elif opcao == '2':
        vaga = int(input("Número da vaga a ser liberada: "))
        condominio.liberar_vaga(vaga)
    elif opcao == '3':
        condominio.imprimir_com_vaga()
    elif opcao == '4':
        condominio.fila_espera.imprimir_fila()
    elif opcao == '5':
        print("Fim.")
        break
    else:
        print("Opção inválida. Tente novamente.")

