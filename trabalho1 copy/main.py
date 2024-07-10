# 1) Construa a classe Torre e a classe Apartamento. A classe Torre deve possuir os atributos id, nome e endereço. A classe Apartamento deve conter os atributos, id, número 
# do apartamento, número da vaga de garagem e torre.
#imports
from Apartamento import Apartamento
from Estacionamento import *
from Torre import Torre

#Instancias
torre1 = Torre(1, 'torresmo', 'torres')
torre1.imprimir()
condominio = Condominio()


#loops
for i in range(1, 11):
    apt = Apartamento(i, f'quarto {i}', torre1)
    condominio.cadastrar_apartamento(apt)

while True:
    print('')
    print('')
    print('')
    print('')
    print('')
    print('')
    print(Fore.GREEN + Style.BRIGHT + '==============================')
    print(Fore.CYAN + Style.BRIGHT + '   __  __  _____  _   _  _   _ ')
    print(Fore.CYAN + Style.BRIGHT + '  |  \/  ||  ___|| \ | || | | |')
    print(Fore.CYAN + Style.BRIGHT + '  | \  / || |__  |  \| || | | |')
    print(Fore.CYAN + Style.BRIGHT + '  | |\/| ||  __| | . ` || | | |')
    print(Fore.CYAN + Style.BRIGHT + '  | |  | || |___ | |\  || |_| |')
    print(Fore.CYAN + Style.BRIGHT + '  |_|  |_|\____/ \_| \_|\_____|')
    print(Fore.GREEN + Style.BRIGHT + '==============================')
    print("1- Cadastrar apartamento")
    print("2- Liberar vaga")
    print("3- Imprimir a lista de apartamentos com vaga")
    print("4- Imprimir a fila de espera")
    print("5- Sair")
    print(Fore.GREEN + Style.BRIGHT + '==============================')
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

